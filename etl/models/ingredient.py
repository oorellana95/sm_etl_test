"""Ingredient data model definition."""
from sqlalchemy import Column, Integer, String

from etl.services.database import Base


class Ingredient(Base):
    """Ingredient table definition."""

    __tablename__ = "ingredient"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
