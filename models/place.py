#!/usr/bin/python3
"""
Inherit from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Inherit from BaseModel.

    Public class attribute:
        city_id type(string).
        user_id type(string).
        name type(string).
        description type(string)
        number_room type(integer)
        number_bathrooms type(integer)
        max_guest type(integer)
        price_by_night type(integer)
        latitude type(float)
        longitude type(float)
        amenity_ids type(list).
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
