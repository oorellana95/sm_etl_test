"""JobTitle data model definition."""
from sqlalchemy import Column, Integer, String

from etl.services.database import Base


class JobTitle(Base):
    """JobTitle table definition."""

    __tablename__ = "job_title"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
