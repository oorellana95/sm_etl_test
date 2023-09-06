"""User data model definition."""
from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String

from etl.services.database import Base


class User(Base):
    """User table definition."""

    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    id_encoded = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    sex = Column(Enum("Male", "Female"), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    birthdate = Column(Date, nullable=False)
    id_job_title = Column(Integer, ForeignKey("job_title.id"), nullable=False)
