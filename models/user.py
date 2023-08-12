#!/usr/bin/python3
"""
A class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    A class User

    Attributes:
        email: Class attribute that holds user email
        Ppassword: Class attribute that holds user password
        first_name: Class attribute that holds user first name
        last_name: Class attribute that holds user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialises a new User instance.
        """
        super().__init__(*args, **kwargs)
