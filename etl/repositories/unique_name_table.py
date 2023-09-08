"""
JobTitles, Tags and Ingredients repository module
"""
from etl.models.ingredient import Ingredient
from etl.models.job_title import JobTitle
from etl.models.tag import Tag
from etl.repositories._repository_functions import apply_session_rollback_decorator


def load_job_titles(db_session, job_titles):
    """Function to load job titles"""
    missing_job_titles = _find_missing_entries(
        db_session=db_session, model=JobTitle, entries=job_titles
    )
    _insert_missing_entries(
        db_session=db_session, model=JobTitle, new_entries=missing_job_titles
    )


def load_tags(db_session, tags):
    """Function to load tags"""
    missing_tags = _find_missing_entries(db_session=db_session, model=Tag, entries=tags)
    _insert_missing_entries(db_session=db_session, model=Tag, new_entries=missing_tags)


def load_ingredients(db_session, ingredients):
    """Function to load ingredients"""
    missing_ingredients = _find_missing_entries(
        db_session=db_session, model=Ingredient, entries=ingredients
    )
    _insert_missing_entries(
        db_session=db_session, model=Ingredient, new_entries=missing_ingredients
    )


def _find_missing_entries(db_session, model, entries):
    """Find missing entities that do not exist in the table"""
    existing_names = [item.name for item in db_session.query(model).all()]
    missing_entities = set(entries) - set(existing_names)
    return missing_entities


@apply_session_rollback_decorator
def _insert_missing_entries(db_session, model, new_entries):
    """Insert missing entries into the table"""
    new_rows = [model(name=entry) for entry in new_entries]
    db_session.add_all(new_rows)
