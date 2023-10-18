"""Model for Artwork"""
from uuid import uuid4

from sqlalchemy import Column, String, Integer, Boolean, Date, Float, ForeignKey

from app.db import Base


class Artwork(Base):
    """Base Model for Artwork"""

    __tablename__ = "artworks"
    id = Column(String(100), primary_key=True, default=uuid4)
    stock = Column(Integer())  # how many pieces in stock currently
    title = Column(String(200), nullable=False)
    description = Column(String(1000))
    dimensions = Column(String(100))
    original = Column(Boolean)  # True for original artworks, false for prints or copies
    artist = Column(String(100), nullable=True)
    creation_date = Column(Date())  # month and year when artwork was created TODO make it without day in date
    price = Column(Float)  # in euros
    image_url = Column(String(2000))  # url for artwork image
    discount = Column(Float)  # current percentage % discount

    category_id = Column(String(100), ForeignKey("categories.id"), default=None)
    technique_id = Column(String(100), ForeignKey("techniques.id"), default=None)

    def __init__(self, stock: int, title: str, description: str, dimensions: str, original: bool, artist: str,
                 creation_date: str, price: float, image_url: str, discount: float, category_id: str = None,
                 technique_id: str = None):
        self.stock = stock
        self.title = title
        self.description = description
        self.dimensions = dimensions
        self.original = original
        self.artist = artist
        self.creation_date = creation_date
        self.price = price
        self.image_url = image_url
        self.discount = discount
        self.category_id = category_id
        self.technique_id = technique_id
