"""
Rating repository module
"""
import pandas as pd

from etl.models.rating import Rating
from etl.repositories.generic_functions import (
    protect_session_with_rollback,
    upsert_data,
)


@protect_session_with_rollback
def load_ratings(db_session, ratings_df: pd.DataFrame):
    """Function to load ratings into the database"""
    #  Rename DataFrame columns to match the target table
    ratings_df = ratings_df.rename(
        columns={
            "user_id": "id_user",
            "recipe_id": "id_recipe",
            "date": "submitted_at",
            "rating": "valuation",
            "review": "review",
        }
    )

    # Convert the DataFrame to a list of dictionaries
    entries = ratings_df.to_dict(orient="records")

    # Upsert the data into the Rating table
    upsert_data(
        db_session=db_session,
        model=Rating,
        new_entries=entries,
        primary_key_names=("id_user", "id_recipe"),
    )
