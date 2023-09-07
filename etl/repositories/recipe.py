"""
Recipe repository module
"""
import pandas as pd

from etl.models.ingredient import Ingredient
from etl.models.recipe import Recipe
from etl.models.recipe_ingredient import RecipeIngredient
from etl.models.recipe_tag import RecipeTag
from etl.models.tag import Tag
from etl.repositories.generic_functions import (
    protect_session_with_rollback,
    upsert_data,
)


@protect_session_with_rollback
def load_recipes(db_session, recipes_df: pd.DataFrame):
    """Function to load recipes into the database"""
    # Drop unnecessary columns
    recipes_df.drop(columns=["n_steps", "n_ingredients"])

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

    # Upsert the data into the Recipe table and its associated tables
    upsert_data(db_session, Recipe, entries)
    upsert_association_recipe_tags(db_session, recipes_df)
    upsert_association_recipe_ingredients(db_session, recipes_df)


def upsert_association_recipe_tags(db_session, recipes_df: pd.DataFrame):
    tag_df = pd.read_sql(
        db_session.query(Tag.id.label("id_tag"), Tag.name.label("name_tag")).statement,
        db_session.bind,
    )

    recipe_tag_mappings = []
    for index, recipe in recipes_df.iterrows():
        for tag in eval(recipe["tags"]):
            id_tag = tag_df.loc[tag_df["name_tag"] == tag, "id_tag"].values[0]
            id_recipe = recipe["id"]
            dictionary = {"id_recipe": id_recipe, "id_tag": id_tag}
            recipe_tag_mappings.append(dictionary)

    upsert_data(
        db_session=db_session,
        model=RecipeTag,
        new_entries=recipe_tag_mappings,
        primary_key_names=("id_recipe", "id_tag"),
    )


def upsert_association_recipe_ingredients(db_session, recipes_df: pd.DataFrame):
    ingredient_df = pd.read_sql(
        db_session.query(
            Ingredient.id.label("id_ingredient"),
            Ingredient.name.label("name_ingredient"),
        ).statement,
        db_session.bind,
    )

    recipe_ingredient_mappings = []
    for index, recipe in recipes_df.iterrows():
        for ingredient in eval(recipe["ingredients"]):
            id_ingredient = ingredient_df.loc[
                ingredient_df["name_ingredient"] == ingredient, "id_ingredient"
            ].values[0]
            id_recipe = recipe["id"]
            dictionary = {"id_recipe": id_recipe, "id_ingredient": id_ingredient}
            recipe_ingredient_mappings.append(dictionary)

    upsert_data(
        db_session=db_session,
        model=RecipeIngredient,
        new_entries=recipe_ingredient_mappings,
        primary_key_names=("id_recipe", "id_ingredient"),
    )
