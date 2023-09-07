"""
JobTitles, Tags and Ingredients repository module
"""
from etl.models.ingredient import Ingredient
from etl.models.job_title import JobTitle
from etl.models.tag import Tag


def load_job_titles(db_session, job_titles):
    """Function to load job titles"""
    _load_unique_name_table(db_session=db_session, model=JobTitle, values=job_titles)


def load_tags(db_session, tags):
    """Function to load tags"""
    _load_unique_name_table(db_session=db_session, model=Tag, values=tags)


def load_ingredients(db_session, ingredients):
    """Function to load ingredients"""
    _load_unique_name_table(db_session=db_session, model=Ingredient, values=ingredients)


def _load_unique_name_table(db_session, model, values):
    """Function to load tables that only have unique names and their identifiers"""
    # Determine the set of missing entries
    missing_entries = set(values) - set(
        [item.name for item in db_session.query(model).all()]
    )

    if missing_entries:
        try:
            # Insert missing entries into the database
            new_rows = [model(name=entry) for entry in missing_entries]
            db_session.add_all(new_rows)
            db_session.commit()
        except Exception as e:
            # In case of an error, rollback any changes made to the database
            db_session.rollback()
            raise e
