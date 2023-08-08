#!/usr/bin/python3
"""
A class BaseModel that defines all common attributes/methods
for other classes.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    A class BaseModel

    Attributes:
        id: public class attribute that generate a unique id
        created_at: public class instance that assigns the current
                    datetime when an instance is created.
        updated_at: public class instance that assigns the current
                    datetime when an instance is created and updated
                    everytime it changes at object.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialising public instance attributes.

        Args:
            args: numbers od argument.
            kwargs: A double pointer to the head or an array of args.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    format_string = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, format_string))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """
        updates the public instance attribute updated_at.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns:
            A dictionary containing all keys/values of __dict__.
        """
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d

    def __str__(self):
        """
        print:
            [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[BaseModel] ({self.id}) {self.__dict__}"
