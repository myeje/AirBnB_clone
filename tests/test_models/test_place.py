#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.place import Place
"""
This is a unittest for class Place.
"""


class TestPlace(unittest.TestCase):
    """Testing with unittest"""
    def test_validate_format(self):
        """This is test that validate format that is string.
        """
        pop = Place()
        self.assertIsInstance(pop.city_id, str)
        self.assertIsInstance(pop.user_id, str)
        self.assertIsInstance(pop.name, str)
        self.assertIsInstance(pop.description, str)
        self.assertIsInstance(pop.number_rooms, int)
        self.assertIsInstance(pop.number_bathrooms, int)
        self.assertIsInstance(pop.max_guest, int)
        self.assertIsInstance(pop.price_by_night, int)
        self.assertIsInstance(pop.latitude, float)
        self.assertIsInstance(pop.longitude, float)
        self.assertIsInstance(pop.amenity_ids, list)

    def test_Place_is_Subclass(self):
        """This is a test for BaseModel subclasses.
        """
        pop = Place()
        pp = pop.__class__
        self.assertTrue(issubclass(pp, BaseModel))

    def test_empty_string(self):
        """This is a test that validate if it is empty or zero.
        """
        pop = Place()
        self.assertEqual(pop.city_id, "")
        self.assertEqual(pop.user_id, "")
        self.assertEqual(pop.name, "")
        self.assertEqual(pop.description, "")
        self.assertEqual(pop.number_rooms, 0)
        self.assertEqual(pop.number_bathrooms, 0)
        self.assertEqual(pop.max_guest, 0)
        self.assertEqual(pop.price_by_night, 0)
        self.assertEqual(pop.latitude, 0.0)
        self.assertEqual(pop.longitude, 0.0)
        self.assertEqual(pop.amenity_ids, [])

    def test_representation_place(self):
        """This is a test that validate the representation of the User.
        """
        pop = Place()
        dit = pop.__dict__
        parse = "[{}] ({}) {}".format(
                pop.__class__.__name__, pop.id, dit)
        self.assertEqual(parse, str(pop))

    def test_create_Place(self):
        """This is a test that validate user creation.
        """
        pop = Place()
        pop.city_id = "758mt9-2314-5678-901fh2"
        pop.user_id = "Pope"
        pop.name = "Gabriel"
        pop.description = "Simple"
        pop.number_rooms = "3"
        pop.number_bathrooms = "2"
        pop.max_guest = "20"
        pop.price_by_night = "30"
        pop.latitude = "6.789034"
        pop.longitude = "51.19905"
        pop.amenity_ids = "heater, soap"
        pop.save()
        self.assertEqual(pop.city_id, "758mt9-2314-5678-901fh2")
        self.assertEqual(pop.user_id, "Pope")
        self.assertEqual(pop.name, "Gabriel")
        self.assertEqual(pop.description, "Simple")
        self.assertEqual(pop.number_rooms, "3")
        self.assertEqual(pop.number_bathrooms, "2")
        self.assertEqual(pop.max_guest, "20")
        self.assertEqual(pop.price_by_night, "30")
        self.assertEqual(pop.latitude, "6.789034")
        self.assertEqual(pop.longitude, "51.19905")
        self.assertEqual(pop.amenity_ids, "heater, soap")

    def test_create_update_Place(self):
        """This is a test that validate attribute value change in update.
        """
        pop = Place()
        pop.city_id = "ChIJrTLr-GyuEmsRBfy61i59si0"
        pop.user_id = "Paolo"
        pop.name = "Huaral"
        lopp = pop.description = "Perfect"
        pop.number_rooms = "1"
        pop.number_bathrooms = "2"
        pop.max_guest = "8"
        pop.price_by_night = "40"
        pop.latitude = "-33.870775"
        pop.longitude = "151.199025"
        pop_amenity = pop.amenity_ids = "good music"
        pop.save()
        lop = pop.description = "Sus"
        pop2_amenity = pop.amenity_ids = "nothing interesting"
        self.assertNotEqual(lopp, lop)
        self.assertNotEqual(pop_amenity, pop2_amenity)
