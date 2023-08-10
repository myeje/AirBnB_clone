#!/usr/bin/python3

"""
Write all those classes that inherit from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Inherits from BaseModel.

    Public class attributes:
        name type (string)
    """
    name = ""
