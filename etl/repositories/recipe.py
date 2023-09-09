"""
Recipe repository module
"""

import pandas as pd
from etl.models.ingredient import Ingredient
from etl.models.recipe import Recipe
from etl.models.recipe_ingredient import RecipeIngredient
from etl.models.recipe_tag import RecipeTag
from etl.models.tag import Tag
from etl.repositories._repository_functions import upsert_data
from etl.repositories.user import fetch_user_ids, insert_placeholder_users_into_db
from etl.services.exports import save_dataframe_to_timestamped_csv
from etl.services.logger import Logger


def load_recipes(db_session, recipes_df: pd.DataFrame):
    """The main function that orchestrates the entire process of loading recipes into the database"""
    processed_df = _preprocess_recipes_data(recipes_df)
    _handle_recipes_missing_mandatory_values(processed_df)
    _upsert_recipes_and_associations(db_session, processed_df)


def fetch_recipe_ids(db_session):
    return [
        result[0] for result in db_session.query(Recipe.id.label("id_recipe")).all()
    ]


def _handle_recipes_missing_mandatory_values(recipes_df):
    """Handle recipes with missing mandatory values"""
    recipes_df_with_nan = recipes_df[recipes_df.isna().any(axis=1)]
    invalid_recipes_count = len(recipes_df_with_nan)
    if invalid_recipes_count:
        file_path = save_dataframe_to_timestamped_csv(
            df=recipes_df_with_nan,
            filename_prefix=f"{invalid_recipes_count}_recipes_missing_mandatory_values",
        )
        Logger.error(
            message=f"A total of {invalid_recipes_count} recipes missing mandatory values have been added to {file_path} for further analysis."
        )


def _preprocess_recipes_data(recipes_df):
    """Preprocess recipes DataFrame for loading into the database"""
    processed_df = recipes_df.drop(columns=["n_steps", "n_ingredients"])
    processed_df = processed_df.rename(
        columns={
            "id": "id",
            "contributor_id": "id_user",
            "name": "name",
            "description": "description",
            "minutes": "minutes",
            "email": "steps",
            "nutrition": "nutrition",
            "submitted": "submitted_at",
        }
    )
    processed_df["description"] = processed_df["description"].replace({pd.NA: ""})

    return processed_df


def _upsert_recipes_and_associations(db_session, processed_df):
    """Upserts recipes and associated data into the database"""
    processed_df = processed_df[~processed_df.isna().any(axis=1)]
    _upsert_recipes(db_session, processed_df)
    _upsert_association_recipe_tags(db_session, processed_df)
    _upsert_association_recipe_ingredients(db_session, processed_df)


def _upsert_recipes(db_session, recipes_df):
    """Upsert recipes into the database"""
    existing_user_ids = fetch_user_ids(db_session)
    _upsert_recipes_with_valid_id_user(db_session, recipes_df, existing_user_ids)
    _handle_recipes_with_invalid_id_user(db_session, recipes_df, existing_user_ids)


def _upsert_recipes_with_valid_id_user(db_session, recipes_df, existing_user_ids):
    """Upsert valid recipes with existing user IDs"""
    valid_recipes_df = recipes_df[recipes_df["id_user"].isin(existing_user_ids)]
    valid_recipe_entries = valid_recipes_df.to_dict(orient="records")
    upsert_data(db_session=db_session, model=Recipe, new_entries=valid_recipe_entries)


def _handle_recipes_with_invalid_id_user(db_session, recipes_df, existing_user_ids):
    """Handle recipes with invalid user IDs"""
    invalid_recipes_df = recipes_df[~recipes_df["id_user"].isin(existing_user_ids)]

    # Check if there are invalid recipes before proceeding with operations
    if not invalid_recipes_df.empty:
        # Insert placeholder users and upsert data for invalid recipes
        insert_placeholder_users_into_db(
            db_session=db_session, new_entries=set(invalid_recipes_df["id_user"])
        )

        # Insert valid recipe entries after creating the placeholder users
        valid_recipe_entries = invalid_recipes_df.to_dict(orient="records")
        upsert_data(
            db_session=db_session, model=Recipe, new_entries=valid_recipe_entries
        )
        Logger.warning(
            message=f"A total of {len(invalid_recipes_df)} blueprint users have been created with the corresponding ids."
        )

        # Save the DataFrame to a CSV file with a timestamped filename
        file_path = save_dataframe_to_timestamped_csv(
            df=invalid_recipes_df, filename_prefix=f"{len(invalid_recipes_df)}_recipes_with_invalid_id_user"
        )
        Logger.warning(
            message=f"A total of {len(invalid_recipes_df)} recipes with invalid user IDs have been added to {file_path} for further analysis."
        )


def _upsert_association_recipe_tags(db_session, recipes_df: pd.DataFrame):
    """Upsert associations between recipes and tags"""
    tags_dic = {tag.name: tag.id for tag in db_session.query(Tag.id, Tag.name).all()}

    recipe_tag_mappings = []

    for index, recipe in recipes_df.iterrows():
        tags = eval(recipe["tags"])

        for tag in tags:
            id_tag = tags_dic.get(tag)
            id_recipe = recipe["id"]
            dictionary = {"id_recipe": id_recipe, "id_tag": id_tag}
            recipe_tag_mappings.append(dictionary)

    upsert_data(
        db_session=db_session,
        model=RecipeTag,
        new_entries=recipe_tag_mappings,
        primary_key_names=("id_recipe", "id_tag"),
    )


def fetch_tags_dataframe(db_session):
    tags_database_df = pd.read_sql(
        db_session.query(Tag.id.label("id_tag"), Tag.name.label("name_tag")).statement,
        db_session.bind,
    )
    return tags_database_df


def _upsert_association_recipe_ingredients(db_session, recipes_df: pd.DataFrame):
    """Upserts associations between recipes and ingredients."""
    ingredients_dic = {
        ingredient.name: ingredient.id
        for ingredient in db_session.query(Ingredient.id, Ingredient.name).all()
    }

    recipe_ingredient_mappings = []

    for index, recipe in recipes_df.iterrows():
        ingredients = eval(recipe["ingredients"])

        for ingredient in ingredients:
            id_ingredient = ingredients_dic.get(ingredient)
            id_recipe = recipe["id"]
            dictionary = {"id_recipe": id_recipe, "id_ingredient": id_ingredient}
            recipe_ingredient_mappings.append(dictionary)

    upsert_data(
        db_session=db_session,
        model=RecipeIngredient,
        new_entries=recipe_ingredient_mappings,
        primary_key_names=("id_recipe", "id_ingredient"),
    )
