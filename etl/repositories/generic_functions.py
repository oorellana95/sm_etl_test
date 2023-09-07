def protect_session_with_rollback(func):
    def wrapper(db_session, *args, **kwargs):
        try:
            return func(db_session, *args, **kwargs)
        except Exception as e:
            # In case of an error, rollback any changes made to the database
            db_session.rollback()
            raise e

    return wrapper


def upsert_data(db_session, model, new_entries, primary_key_name="id"):
    # Extract primary key values from new entries
    new_primary_key_values = [entry.get(primary_key_name) for entry in new_entries]

    # Query for existing entries using the primary key values
    existing_entries = (
        db_session.query(model)
        .filter(getattr(model, primary_key_name).in_(new_primary_key_values))
        .all()
    )

    # Create a dictionary to efficiently access existing entries by primary key
    existing_entries_dict = {
        getattr(existing_entry, primary_key_name): existing_entry
        for existing_entry in existing_entries
    }

    # Prepare a list for new entries to be inserted
    entries_to_insert = []

    # Iterate through new entries and perform upsert
    for new_entry in new_entries:
        primary_key_value = new_entry.get(primary_key_name)
        existing_entry = existing_entries_dict.get(primary_key_value)

        if existing_entry:
            # Update existing entry with new data
            for key, value in new_entry.items():
                setattr(existing_entry, key, value)
        else:
            # Add new entry to the list for bulk insertion
            entries_to_insert.append(new_entry)

    # Bulk insert new entries if there are any
    if entries_to_insert:
        db_session.bulk_insert_mappings(model, entries_to_insert)

    # Commit changes to the database session
    db_session.commit()
