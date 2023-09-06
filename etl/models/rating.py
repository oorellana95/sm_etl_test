"""Rating data model definition."""
from sqlalchemy import CheckConstraint, Column, Date, ForeignKey, Integer, String

from etl.services.database import Base


class Rating(Base):
    """Rating table definition."""

    __tablename__ = "rating"
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey("user.id"), nullable=False)
    id_recipe = Column(Integer, ForeignKey("recipe.id"), nullable=False)
    valuation = Column(
        Integer, CheckConstraint("0<=`valuation` AND `valuation`<=2"), nullable=False
    )
    review = Column(String(255), nullable=True)
    submitted_at = Column(Date, nullable=False)
