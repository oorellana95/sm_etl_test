"""
User data SQLAlchemy model
"""
from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String

from etl.services.database import Base


class User(Base):
    """User table definition."""

    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    id_encoded = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    sex = Column(Enum("Male", "Female"), nullable=True)
    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    birthdate = Column(Date, nullable=False)
    id_job_title = Column(Integer, ForeignKey("job_title.id"), nullable=True)


placeholder_not_specified_user = {
    "id": None,
    "id_encoded": "sm00000000",
    "first_name": "Source",
    "last_name": "Meridian",
    "sex": None,
    "email": "no.user@sm.com",
    "phone": "000-000-0000",
    "birthdate": "2000-01-01",
    "id_job_title": None,
}
