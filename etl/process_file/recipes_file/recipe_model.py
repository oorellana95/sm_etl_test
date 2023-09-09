"""
Recipe data SQLAlchemy model
"""
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.mysql import JSON

from etl.services.sql_alchemy.database import Base


class Recipe(Base):
    """Recipe table definition."""

    __tablename__ = "recipe"
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey("user.id"), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    minutes = Column(Integer, nullable=False)
    steps = Column(JSON, nullable=False)
    nutrition = Column(JSON, nullable=False)
    submitted_at = Column(Date, nullable=False)

    def to_dict(self):
        """Convert Recipe object to a dictionary."""
        return {
            "id": self.id,
            "id_user": self.id_user,
            "name": self.name,
            "description": self.description,
            "minutes": self.minutes,
            "steps": self.steps,
            "nutrition": self.nutrition,
            "submitted_at": str(self.submitted_at),  # Convert Date to string if needed
        }
