#!/usr/bin/python3
"""
Inhert from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherites from BaseModel

    Public class attributes:
        state_id type(string)
        name type(string)
    """
    state_id = ""
    name = ""
