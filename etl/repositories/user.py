"""
User repository module
"""
import pandas as pd
from etl.models.job_title import JobTitle
from etl.models.user import User, placeholder_not_specified_user
from etl.repositories.generic_functions import (
    protect_session_with_rollback,
    upsert_data,
)


@protect_session_with_rollback
def insert_placeholder_users_into_db(db_session, new_user_ids):
    entries_to_insert = []

    for user_id in new_user_ids:
        user_dict = placeholder_not_specified_user.copy()
        user_dict["id"] = user_id
        entries_to_insert.append(user_dict)

    db_session.bulk_insert_mappings(User, entries_to_insert)
    db_session.commit()


@protect_session_with_rollback
def load_users(db_session, users_df: pd.DataFrame):
    users_df = _merge_id_job_titles(db_session, users_df)
    entries = users_df.to_dict(orient="records")
    upsert_data(db_session, User, entries)


def fetch_job_titles_dataframe(db_session):
    """Fetch job titles from the database"""
    job_titles_df = pd.read_sql(
        db_session.query(
            JobTitle.id.label("id_job_title"), JobTitle.name.label("name_job_title")
        ).statement,
        db_session.bind,
    )
    return job_titles_df


def fetch_user_ids(db_session):
    return db_session.query(User.id.label("id_user")).all()


def _merge_id_job_titles(db_session, users_df: pd.DataFrame):
    """Merge users_df with job titles from the database"""
    job_titles_df = fetch_job_titles_dataframe(db_session)
    users_df = _merge_users_and_job_titles(users_df, job_titles_df)
    users_df = _preprocess_merged_data(users_df)
    return users_df


def _merge_users_and_job_titles(users_df, job_titles_df):
    """Merge users_df with job_titles_df"""
    users_df = pd.merge(
        users_df,
        job_titles_df,
        left_on="job title",
        right_on="name_job_title",
        how="left",
    )
    return users_df


def _preprocess_merged_data(users_df):
    """Preprocess the merged DataFrame"""
    users_df = users_df.drop(columns=["job title", "name_job_title"])
    users_df = users_df.rename(
        columns={
            "user id": "id",
            "encoded id": "id_encoded",
            "first name": "first_name",
            "last name": "last_name",
            "Sex": "sex",
            "email": "email",
            "phone": "phone",
            "date of birth": "birthdate",
            "id_job_title": "id_job_title",
        }
    )
    return users_df
