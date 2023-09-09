"""
RecipeIngredient data SQLAlchemy model
"""
from sqlalchemy import Column, ForeignKey, Integer

from etl.services.sql_alchemy.database import Base


class RecipeIngredient(Base):
    """RecipeIngredient table definition."""

    __tablename__ = "recipe_ingredient"
    id_recipe = Column(Integer, ForeignKey("recipe.id"), primary_key=True)
    id_ingredient = Column(Integer, ForeignKey("ingredient.id"), primary_key=True)

    def to_dict(self):
        """Convert RecipeIngredient object to a dictionary."""
        return {
            "id_recipe": self.id_recipe,
            "id_ingredient": self.id_ingredient,
        }
