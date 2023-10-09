"""Model for user"""
from uuid import uuid4

from sqlalchemy import Column, String, Boolean

from app.db import Base


class User(Base):
    """User Model class"""

    __tablename__ = "user"
    id = Column(String(100), primary_key=True, default=uuid4)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    superuser = Column(Boolean, default=False)
    name = Column(String(50))
    surname = Column(String(50))
    phone = Column(String(15))
    address = Column(String(100))
    city = Column(String(50))
    country = Column(String(50))
    postal_code = Column(String(10))

