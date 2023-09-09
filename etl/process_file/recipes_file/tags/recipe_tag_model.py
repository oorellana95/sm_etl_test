"""
RecipeTag data SQLAlchemy model
"""
from sqlalchemy import Column, ForeignKey, Integer

from etl.services.sql_alchemy.database import Base


class RecipeTag(Base):
    """RecipeTag table definition."""

    __tablename__ = "recipe_tag"
    id_recipe = Column(Integer, ForeignKey("recipe.id"), primary_key=True)
    id_tag = Column(Integer, ForeignKey("tag.id"), primary_key=True)

    def to_dict(self):
        """Convert RecipeTag instance to a dictionary."""
        return {
            "id_recipe": self.id_recipe,
            "id_tag": self.id_tag,
        }
