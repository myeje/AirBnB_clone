#!/usr/bin/python3
"""
A class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances.
"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file.

    Args:
        file_path: private instances attributes.
        objects: private instance attributes.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns:
            the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                from models.base_model import BaseModel

                for key, value in data.items():
                    class_name = value['__class__']
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
