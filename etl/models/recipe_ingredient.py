"""
RecipeIngredient data SQLAlchemy model
"""
from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint, String

from etl.services.database import Base


class RecipeIngredient(Base):
    """RecipeIngredient table definition."""

    __tablename__ = "recipe_ingredient"
    id_recipe = Column(Integer, ForeignKey("recipe.id"), primary_key=True)
    id_ingredient = Column(Integer, ForeignKey("ingredient.id"), primary_key=True)
