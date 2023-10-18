"""Model for Category"""
from uuid import uuid4

from sqlalchemy import Column, String

from app.db import Base


class Category(Base):
    """Base Model for Category"""

    __tablename__ = "categories"
    id = Column(String(100), primary_key=True, default=uuid4)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(500), nullable=True)

    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description
