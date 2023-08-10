#!/usr/bin/python3

"""
Inherit from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherit from BaseModel.

    Public class attributes:
        place_id type(string)
        user_id type(string)
        text type(string)
    """
    place_id = ""
    user_id = ""
    text = ""
