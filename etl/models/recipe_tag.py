"""RecipeTag data model definition."""
from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint

from etl.services.database import Base


class RecipeTag(Base):
    """RecipeTag table definition."""

    __tablename__ = "recipe_tag"
    id_recipe = Column(Integer, ForeignKey("recipe.id"), primary_key=True)
    id_tag = Column(Integer, ForeignKey("tag.id"), primary_key=True)
