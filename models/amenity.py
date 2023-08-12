#!/usr/bin/python3
"""
Inherit from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Inherit from BaseModel

    Public class attributes:
        name type(string)
    """
    name = ""
