from etl.models.ingredient import Ingredient
from etl.models.job_title import JobTitle
from etl.models.tag import Tag


def load_job_titles(db_session, job_titles):
    _load_unique_name_table(db_session=db_session, model=JobTitle, values=job_titles)


def load_tags(db_session, tags):
    _load_unique_name_table(db_session=db_session, model=Tag, values=tags)


def load_ingredients(db_session, ingredients):
    _load_unique_name_table(db_session=db_session, model=Ingredient, values=ingredients)


def _load_unique_name_table(db_session, model, values):
    """Function to load tables that only have unique names and its identifiers"""
    values_to_insert = set(values)
    values_from_database = set(
        [job_title.name for job_title in db_session.query(model).all()]
    )
    missing_entries = values_to_insert - values_from_database

    if missing_entries:
        try:
            for entry in missing_entries:
                new_row = model(name=entry)
                db_session.add(new_row)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            raise e
