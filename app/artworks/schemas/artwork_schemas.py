"""Artwork schemas"""

from pydantic import BaseModel, UUID4


class ArtworkSchema(BaseModel):
    """Base Schema for Artwork"""

    id: UUID4
    stock: int
    title: str
    description: str
    dimensions: str
    original: bool
    artist: str
    creation_date: str
    price: float
    image_url: str
    discount: float
    category_id: str
    technique_id: str
