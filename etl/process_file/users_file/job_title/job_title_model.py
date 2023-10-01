"""
JobTitle data SQLAlchemy model
"""
from sqlalchemy import Column, Integer, String

from etl.services.sql_alchemy.database import Base


class JobTitle(Base):
    """JobTitle table definition."""

    __tablename__ = "job_title"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)

    def to_dict(self):
        """Convert JobTitle object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
        }
