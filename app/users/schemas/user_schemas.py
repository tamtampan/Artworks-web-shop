"""User Schemas module"""
from typing import Optional

from pydantic import BaseModel, UUID4, EmailStr


class UserSchema(BaseModel):
    """Base schema for User"""

    id: UUID4
    email: str
    password_hashed: str
    first_name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    city: Optional[str]
    country: Optional[str]
    postal_code: Optional[str]
    total_cost_wish_list: float
    date_subscribed: str
    active: bool
    superuser: bool
    verification_code: Optional[int]

    class Config:
        """Configuration Class"""
        orm_mode = True


class UserSchemaOut(BaseModel):
    """User Out schema"""

    id: UUID4
    email: str
    first_name: str
    last_name: str
    phone: Optional[str]
    address: Optional[str]
    city: Optional[str]
    country: Optional[str]
    postal_code: Optional[str]
    total_cost_wish_list: float
    date_subscribed: str
    is_active: bool
    is_superuser: bool
    verification_code: Optional[int]

    class Config:
        """Configuration Class"""
        orm_mode = True


class UserRegistrationSchema(BaseModel):
    """Base User schema for input"""
    email: EmailStr
    password: str

    class Config:
        """Configuration Class"""
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "dummy@gmail.com",
                "password": "password",
            }
        }


class UserLoginSchema(BaseModel):
    """Login User Schema"""
    email: str
    password: str

    class Config:
        """Configuration Class"""
        schema_extra = {
            "example": {
                "email": "dummy@gmail.com",
                "password": "password"
            }
        }


class ChangePasswordSchema(BaseModel):
    """User schema for password change"""
    code: int
    new_password: str
    repeat_password: str

    class Config:
        """Configuration Class"""
        schema_extra = {
            "example": {
                "code": 123456,
                "new_password": "new_password",
                "repeat_password": "repeat_password"
            }
        }


# class UserUpdateSchema(BaseModel):
#     """User schema for update"""
#     first_name: str
#     last_name: str
#     email: str
#
#     class Config:
#         """Configuration Class"""
#         schema_extra = {
#             "example": {
#                 "first_name": "John",
#                 "last_name": "Doe",
#                 "email": "dummy@gmail.com"
#             }
#         }

class UserSchemaFillIn(BaseModel):
    """Base schema for User information"""

    first_name: str
    last_name: str
    phone: str
    address: str
    city: str
    country: str
    postal_code: str

    # class Config:
    #     """Configuration Class"""
    #     schema_extra = {
    #         "example": {
    #             "first_name": "first_name",
    #             "last_name": "last_name",
    #             "phone": "+381 60 000 0000",
    #             "address": "address",
    #             "city": "city",
    #             "country": "country",
    #             "postal_code": "postal_code"
    #         }
    #     }
    #