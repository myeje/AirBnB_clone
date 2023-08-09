#!/usr/bin/python3
"""
A class User that inherits from BaseModel
"""

from models.base_model import BaseModel
from models import storage

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

    def __str__(self):
        """
        print:
            [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
