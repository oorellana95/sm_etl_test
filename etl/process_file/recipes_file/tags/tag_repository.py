"""
Tags repository module
"""
from etl.process_file.recipes_file.tags.tag_model import Tag
from etl.services.sql_alchemy.repository_functions import (
    find_missing_entries,
    insert_missing_entries,
)


def load_tags(db_session, tags):
    """Function to load tags"""
    missing_tags = find_missing_entries(db_session=db_session, model=Tag, entries=tags)
    insert_missing_entries(db_session=db_session, model=Tag, new_entries=missing_tags)
