"""
SQLAlchemy Database
"""
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from etl.config import config

# Declarative base.
Base = declarative_base()

# Retrieve database uri
database_uri = (
    f"{config.database_config['DATABASE_DIALECT']}://{config.database_config['DATABASE_USER']}:{config.database_config['DATABASE_PASSWORD']}"
    f"@{config.database_config['DATABASE_HOST']}:{config.database_config['DATABASE_PORT']}/{config.database_config['DATABASE_NAME']}"
)

# Session local
engine = create_engine(database_uri)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


@contextmanager
def create_database_session():
    """Get database local session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_database_tables() -> None:
    """Creates a database from the models."""
    Base.metadata.create_all(engine)
