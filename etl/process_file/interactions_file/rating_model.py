"""
Rating data SQLAlchemy model
"""
from sqlalchemy import CheckConstraint, Column, Date, ForeignKey, Integer, Text

from etl.services.sql_alchemy.database import Base


class Rating(Base):
    """Rating table definition."""

    __tablename__ = "rating"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey("user.id"), nullable=False)
    id_recipe = Column(Integer, ForeignKey("recipe.id"), nullable=False)
    valuation = Column(
        Integer, CheckConstraint("0<=`valuation` AND `valuation`<=5"), nullable=False
    )
    review = Column(Text, nullable=True)
    submitted_at = Column(Date, nullable=False)

    def to_dict(self):
        """Convert Rating object to a dictionary."""
        return {
            "id": self.id,
            "id_user": self.id_user,
            "id_recipe": self.id_recipe,
            "valuation": self.valuation,
            "review": self.review,
            "submitted_at": str(self.submitted_at),  # Convert Date to string if needed
        }
