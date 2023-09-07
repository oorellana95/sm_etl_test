from sqlalchemy import tuple_


def protect_session_with_rollback(func):
    def wrapper(db_session, *args, **kwargs):
        try:
            return func(db_session, *args, **kwargs)
        except Exception as e:
            # In case of an error, rollback any changes made to the database
            db_session.rollback()
            raise e

    return wrapper


def upsert_data(db_session, model, new_entries, primary_key_names=("id",)):
    """Main upsert_data function that orchestrates the upsert process"""
    existing_entries_dict = _query_existing_entries_dict(
        db_session, model, primary_key_names, new_entries
    )
    _upsert_entries(
        db_session, model, new_entries, existing_entries_dict, primary_key_names
    )


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


def _upsert_entries(
    db_session, model, new_entries, existing_entries_dict, primary_key_names
):
    """Function to upsert new entries into the database"""
    entries_to_insert = []

    for new_entry in new_entries:
        primary_key_values = tuple(new_entry.get(key) for key in primary_key_names)
        existing_entry = existing_entries_dict.get(primary_key_values)

        if existing_entry:
            # Update existing entry with new data
            for key, value in new_entry.items():
                setattr(existing_entry, key, value)
        else:
            # Add new entry to the list for bulk insertion
            entries_to_insert.append(new_entry)

    # Bulk insert new entries into the database
    if entries_to_insert:
        db_session.bulk_insert_mappings(model, entries_to_insert)

    db_session.commit()
