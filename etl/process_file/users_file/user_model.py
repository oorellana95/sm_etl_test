"""
User data SQLAlchemy model
"""
from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String

from etl.services.sql_alchemy.database import Base


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

    def to_dict(self):
        """Convert User object to a dictionary."""
        return {
            "id": self.id,
            "id_encoded": self.id_encoded,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "email": self.email,
            "phone": self.phone,
            "birthdate": self.birthdate.isoformat(),
            "id_job_title": self.id_job_title,
        }


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
