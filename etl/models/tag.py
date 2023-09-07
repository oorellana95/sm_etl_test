"""
Tag data SQLAlchemy model
"""
from sqlalchemy import Column, Integer, String

from etl.services.database import Base


class Tag(Base):
    """Tag table definition."""

    __tablename__ = "tag"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
