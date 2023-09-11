"""
Rating repository module
"""
import pandas as pd
from etl.process_file.interactions_file.rating_model import Rating
from etl.process_file.recipes_file.recipe_repository import fetch_recipe_ids
from etl.process_file.users.user_repository import (
    fetch_user_ids,
    insert_placeholder_users_into_db,
)
from etl.services.logger import Logger
from etl.services.pandas.exports import (
    handle_dataframe_missing_mandatory_values,
    save_dataframe_to_timestamped_csv,
)
from etl.services.sql_alchemy.repository_functions import upsert_data


def load_ratings(db_session, ratings_df: pd.DataFrame):
    """Function to load ratings into the database"""
    processed_df = _preprocess_ratings_data(ratings_df)
    existing_recipe_ids = fetch_recipe_ids(db_session)

    valid_ratings_df = _filter_invalid_ratings(processed_df, existing_recipe_ids)

    existing_user_ids = fetch_user_ids(db_session)
    _upsert_valid_ratings(db_session, valid_ratings_df, existing_user_ids)


def _filter_invalid_ratings(processed_df, existing_recipe_ids):
    """Filter out invalid ratings"""
    handle_dataframe_missing_mandatory_values(
        df=processed_df, prefix_filename="ratings"
    )
    processed_df = processed_df[~processed_df.isna().any(axis=1)]
    _handle_ratings_with_invalid_id_recipe(processed_df, existing_recipe_ids)
    valid_ratings_df = processed_df[processed_df["id_recipe"].isin(existing_recipe_ids)]
    return valid_ratings_df


def _handle_ratings_with_invalid_id_recipe(ratings_df, existing_recipe_ids):
    """Handle ratings with invalid recipe IDs"""
    invalid_ratings_df = ratings_df[~ratings_df["id_recipe"].isin(existing_recipe_ids)]
    invalid_ratings_count = len(invalid_ratings_df)
    if invalid_ratings_count:
        Logger.warning(
            message=f"There are {invalid_ratings_count} ratings with invalid recipe IDs."
        )
        file_path = save_dataframe_to_timestamped_csv(
            df=invalid_ratings_df,
            filename_prefix=f"{invalid_ratings_count}_ratings_with_invalid_id_recipe",
        )
        Logger.warning(
            message=f"Ratings with invalid recipe IDs have been added to {file_path} for further analysis."
        )


def _upsert_valid_ratings(db_session, valid_ratings_df, existing_user_ids):
    """Upsert valid ratings into the database"""
    _upsert_ratings_df_with_valid_id_user(
        db_session, valid_ratings_df, existing_user_ids
    )
    _handle_ratings_with_invalid_id_user(
        db_session, valid_ratings_df, existing_user_ids
    )


def _upsert_ratings_df_with_valid_id_user(db_session, ratings_df, existing_user_ids):
    """Upsert valid ratings with existing user IDs"""
    valid_ratings_df = ratings_df[ratings_df["id_user"].isin(existing_user_ids)]
    valid_ratings_entries = valid_ratings_df.to_dict(orient="records")
    upsert_data(
        db_session=db_session,
        new_entries=valid_ratings_entries,
        model=Rating,
        primary_key_names=("id_user", "id_recipe"),
    )


def _handle_ratings_with_invalid_id_user(db_session, ratings_df, existing_user_ids):
    """Handle ratings with invalid user IDs"""
    invalid_ratings_df = ratings_df[~ratings_df["id_user"].isin(existing_user_ids)]
    invalid_ratings_count = len(invalid_ratings_df)

    # Check if there are invalid ratings before proceeding with operations
    if invalid_ratings_count:
        # Insert placeholder users and upsert data for invalid ratings
        new_placeholder_users = set(invalid_ratings_df["id_user"])
        insert_placeholder_users_into_db(
            db_session=db_session, new_entries=new_placeholder_users
        )
        Logger.warning(
            message=f"A total of {len(new_placeholder_users)} blueprint users have been created with the corresponding ids."
        )

        # Insert valid ratings entries after creating the placeholder users
        valid_ratings_entries = invalid_ratings_df.to_dict(orient="records")
        upsert_data(
            db_session=db_session,
            model=Rating,
            new_entries=valid_ratings_entries,
            primary_key_names=("id_user", "id_recipe"),
        )

        # Save the DataFrame to a CSV file with a timestamped filename
        file_path = save_dataframe_to_timestamped_csv(
            df=invalid_ratings_df,
            filename_prefix=f"{invalid_ratings_count}_ratings_with_invalid_id_user",
        )
        Logger.warning(
            message=f"A total of {invalid_ratings_count} ratings with invalid user IDs have been added to {file_path} for further analysis."
        )


def _preprocess_ratings_data(ratings_df):
    """Preprocess ratings DataFrame for loading into the database"""
    processed_df = ratings_df.rename(
        columns={
            "user_id": "id_user",
            "recipe_id": "id_recipe",
            "date": "submitted_at",
            "rating": "valuation",
            "review": "review",
        }
    )
    processed_df["review"] = ratings_df["review"].replace({pd.NA: ""})

    return processed_df
