"""Model for user"""
from uuid import uuid4
from datetime import date

from sqlalchemy import Column, String, Boolean, Date, Integer, Float, ForeignKey

from app.db import Base


class User(Base):
    """Base Model for User"""

    __tablename__ = "users"
    id = Column(String(100), primary_key=True, default=uuid4)
    email = Column(String(100), unique=True, nullable=False)
    password_hashed = Column(String(100))
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone = Column(String(15))
    address = Column(String(100))
    city = Column(String(50))
    postal_code = Column(String(10))
    total_cost_wish_list = Column(Float(), default=0)  # automatically summed when item added to wish list
    date_subscribed = Column(Date(), default=date.today())  # automatically filled when user register
    active = Column(Boolean, default=True)
    superuser = Column(Boolean, default=False)
    verification_code = Column(Integer(), nullable=True)

    country_id = Column(String(50), ForeignKey("countries.id"), default=None)

    def __init__(self, email: str, password_hashed: str, first_name: str, last_name: str, phone: str, address: str,
                 city: str, country_id: str, postal_code: str, total_cost_wish_list: float = 0, date_subscribed: str =
                 date.today(), active: bool = True, superuser: bool = False, verification_code: int = None):
        self.email = email
        self.password_hashed = password_hashed
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.city = city
        self.country_id = country_id
        self.postal_code = postal_code
        self.total_cost_wish_list = total_cost_wish_list
        self.date_subscribed = date_subscribed
        self.active = active
        self.superuser = superuser
        self.verification_code = verification_code
