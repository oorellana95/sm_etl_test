"""
Recipe data SQLAlchemy model
"""
from sqlalchemy import CheckConstraint, Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.mysql import JSON

from etl.services.database import Base


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
