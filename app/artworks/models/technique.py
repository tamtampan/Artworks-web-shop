"""Model for Technique"""
from uuid import uuid4

from sqlalchemy import Column, String

from app.db import Base


class Technique(Base):
    """Base Model for Technique"""

    __tablename__ = "techniques"
    id = Column(String(100), primary_key=True, default=uuid4)
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=True)

    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description
