"""Schemas for Categories"""
from typing import Optional

from pydantic import BaseModel, UUID4


class CategorySchema(BaseModel):
    """Base Schema for Category"""

    id: UUID4
    name: str
    description: Optional[str]

    class Config:
        """Configuration Class"""
        orm_mode = True


class CategorySchemaIn(BaseModel):
    """Base Schema In for Category"""

    name: str
    description: Optional[str]

    class Config:
        """Configuration Class"""
        orm_mode = True
