"""Model for Country"""
from uuid import uuid4

from sqlalchemy import Column, String

from app.db import Base


class Country(Base):
    """Base model for Country"""

    __tablename__ = "countries"
    id = Column(String(100), primary_key=True, default=uuid4)
    name = Column(String(100), nullable=False, unique=True)

    def __init__(self, name: str):
        self.name = name
