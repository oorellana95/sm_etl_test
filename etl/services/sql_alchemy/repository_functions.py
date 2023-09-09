from sqlalchemy import tuple_

from etl.config import DATABASE_BATCH_SIZE
from etl.exceptions.file_processing_exeptions.database_load_file_processing_error import (
    DatabaseTransactionError,
)
from etl.services.logger import Logger


def apply_session_rollback_decorator(func):
    """
    Decorator function that applies session rollback on exceptions.

    Functions using this decorator should pass arguments as keywords.
    `db_session` and `new_entries` are mandatory parameters.

    Example usage:
        @apply_session_rollback_decorator
        def my_function(db_session=db_session, new_entries, arg1=value1, arg2=value2):
            # Function implementation
    """

    def wrapper(db_session, new_entries, *args, **kwargs):
        errors = []
        new_entries_list = list(new_entries)
        for i in range(0, len(new_entries), DATABASE_BATCH_SIZE):
            batch = new_entries_list[i : i + DATABASE_BATCH_SIZE]
            errors = []
            try:
                # Split the data into batches
                func(db_session=db_session, new_entries=batch, *args, **kwargs)
                db_session.commit()
            except Exception as e:
                # In case of an error, rollback any changes made to the database
                db_session.rollback()
                errors.append(
                    {
                        "error_number": len(errors),
                        "batch": f"{i}:{i + DATABASE_BATCH_SIZE}",
                        "error_message": e,
                    }
                )
                break

        if errors:
            raise DatabaseTransactionError(
                message=f"An amount of {len(errors)} has been registered while loading data",
                multiple_errors=errors,
            )

    return wrapper


def find_missing_entries(db_session, model, entries):
    """Find missing entities that do not exist in the table"""
    existing_names = [item.name for item in db_session.query(model).all()]
    missing_entities = set(entries) - set(existing_names)
    return missing_entities


@apply_session_rollback_decorator
def insert_missing_entries(db_session, model, new_entries):
    """Insert missing entries into the table"""
    new_rows = [model(name=entry) for entry in new_entries]
    db_session.add_all(new_rows)


@apply_session_rollback_decorator
def upsert_data(db_session, new_entries, model, primary_key_names=("id",)):
    """Function to upsert new entries into the database"""
    existing_entries_dict = _query_existing_entries_dict(
        db_session, model, primary_key_names, new_entries
    )

    entries_to_insert = []

    for new_entry in new_entries:
        primary_key_values = tuple(new_entry.get(key) for key in primary_key_names)
        existing_entry = existing_entries_dict.get(primary_key_values)

        if existing_entry:
            # Check if any attributes of the existing entry differ from the new entry and update if they differ
            if existing_entry.to_dict() != new_entry:
                for key, value in new_entry.items():
                    setattr(existing_entry, key, value)
        else:
            # Add new entry to the list for bulk insertion
            entries_to_insert.append(new_entry)

    # Bulk insert new entries into the database
    if entries_to_insert:
        db_session.bulk_insert_mappings(model, entries_to_insert)


def _query_existing_entries_dict(db_session, model, primary_key_names, new_entries):
    """Query existing entries using primary key values and returns a dictionary with primary_key as key"""
    # Extract primary key values from new entries
    new_primary_key_values = [
        tuple(entry.get(key) for key in primary_key_names) for entry in new_entries
    ]

    # Query existing entries using primary key values
    existing_entries = (
        db_session.query(model)
        .filter(
            tuple_(*(getattr(model, key) for key in primary_key_names)).in_(
                new_primary_key_values
            )
        )
        .all()
    )
    # Create a dictionary to efficiently access existing entries by primary key
    existing_entries_dict = {
        tuple(getattr(existing_entry, key) for key in primary_key_names): existing_entry
        for existing_entry in existing_entries
    }
    return existing_entries_dict
