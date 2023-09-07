"""
Rating repository module
"""
import pandas as pd

from etl.models.rating import Rating
from etl.repositories.generic_functions import upsert_data, protect_session_with_rollback


@protect_session_with_rollback
def load_recipes(db_session, ratings_df: pd.DataFrame):
    """Function to load recipes into the database"""
    #  Rename DataFrame columns to match the target table
    ratings_df = ratings_df.rename(
        columns={
            "id": "id",
            "contributor_id": "id_user",
            "name": "name",
            "description": "description",
            "minutes": "minutes",
            "email": "steps",
            "nutrition": "nutrition",
            "date of birth": "calorie_level",
            "submitted": "submitted_at",
        }
    )

    # Convert the DataFrame to a list of dictionaries
    entries = ratings_df.to_dict(orient="records")

    # Upsert the data into the Recipe table
    upsert_data(db_session, Rating, entries)

