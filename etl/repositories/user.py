"""
User repository module
"""
import pandas as pd

from etl.models.job_title import JobTitle
from etl.models.user import User
from etl.repositories.generic_functions import (
    protect_session_with_rollback,
    upsert_data,
)


@protect_session_with_rollback
def load_users(db_session, users_df: pd.DataFrame):
    # Load job titles and merge id_job_title with users
    users_df = merge_id_job_titles(db_session, users_df)

    # Convert the DataFrame to a list of dictionaries
    entries = users_df.to_dict(orient="records")

    # Upsert the data into the User table
    upsert_data(db_session, User, entries)


def merge_id_job_titles(db_session, users_df: pd.DataFrame):
    """Merge users_df with job titles from the database"""
    job_titles_df = pd.read_sql(
        db_session.query(
            JobTitle.id.label("id_job_title"), JobTitle.name.label("name_job_title")
        ).statement,
        db_session.bind,
    )

    # Merge users_df with job_titles_df
    users_df = pd.merge(
        users_df,
        job_titles_df,
        left_on="job title",
        right_on="name_job_title",
        how="left",
    )

    # Drop unnecessary columns and rename columns
    users_df = users_df.drop(columns=["job title", "name_job_title"]).rename(
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
