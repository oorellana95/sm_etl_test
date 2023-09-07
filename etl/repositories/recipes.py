"""
Recipe repository module
"""
import pandas as pd

from etl.models.recipe import Recipe
from etl.repositories.generic_functions import upsert_data


def load_recipes(db_session, recipes_df: pd.DataFrame):
    """Function to load recipes into the database"""
    try:
        #  Rename DataFrame columns to match the target table
        recipes_df = recipes_df.rename(
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
        entries = recipes_df.to_dict(orient="records")

        # Upsert the data into the Recipe table
        upsert_data(db_session, Recipe, entries)

    except Exception as e:
        # In case of an error, rollback any changes made to the database
        db_session.rollback()
        raise e
