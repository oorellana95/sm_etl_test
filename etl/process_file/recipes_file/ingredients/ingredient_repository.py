"""
Ingredients repository module
"""
from etl.process_file.recipes_file.ingredients.ingredient_model import Ingredient
from etl.services.sql_alchemy.repository_functions import (
    find_missing_entries,
    insert_missing_entries,
)


def load_ingredients(db_session, ingredients):
    """Function to load ingredients"""
    missing_ingredients = find_missing_entries(
        db_session=db_session, model=Ingredient, entries=ingredients
    )
    insert_missing_entries(
        db_session=db_session, model=Ingredient, new_entries=missing_ingredients
    )
