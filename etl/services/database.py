"""SQLAlchemy Database."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from etl import config
from etl.config import (
    DATABASE_DIALECT,
    DATABASE_HOST,
    DATABASE_NAME,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_USER,
)

# Declarative base.
Base = declarative_base()

# Retrieve database uri
database_uri = (
    f"{DATABASE_DIALECT}://{DATABASE_USER}:{DATABASE_PASSWORD}"
    f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

# Session local
engine = create_engine(database_uri)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    """Get database local session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_db() -> None:
    Base.metadata.create_all(engine)
