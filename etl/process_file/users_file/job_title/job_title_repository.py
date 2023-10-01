"""
Tags repository module
"""
from etl.process_file.users_file.job_title.job_title_model import JobTitle
from etl.services.sql_alchemy.repository_functions import (
    find_missing_entries,
    insert_missing_entries,
)


def load_job_titles(db_session, job_titles):
    """Function to load job titles"""
    missing_job_titles = find_missing_entries(
        db_session=db_session, model=JobTitle, entries=job_titles
    )
    insert_missing_entries(
        db_session=db_session, model=JobTitle, new_entries=missing_job_titles
    )
