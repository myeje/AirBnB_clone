#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City
"""
This is a unittest for class City
"""


class TestCity(unittest.TestCase):
    """Testing with unittest"""
    def test_validate_format(self):
        """This is a test that validate the format that is string
        """
        metropolis = City()
        self.assertIsInstance(metropolis.name, str)
        self.assertIsInstance(metropolis.state_id, str)

    def test_City_is_Subclass(self):
        """This is a test for BaseModel subclasses
        """
        metropolis = City()
        pop = metropolis.__class__
        self.assertTrue(issubclass(pop, BaseModel))

    def test_empty_string(self):
        """This is a test that validate if it is empty
        """
        metropolis = City()
        self.assertEqual(metropolis.name, "")
        self.assertEqual(metropolis.state_id, "")

    def test_representation_state(self):
        """This is a test to validate the representation of the User class.
        """
        metropolis = City()
        pop = metropolis.__dict__
        lop = "[{}] ({}) {}".format(metropolis.__class__.__name__,
                                                      metropolis.id, pop)
        self.assertEqual(lop, str(metropolis))

    def test_create_City(self):
        """This is a test that validate user creation.
        """
        metropolis = City()
        metropolis.name = "Rio de Janeiro"
        metropolis.state_id = "0132-7890-6803"
        self.assertEqual(metropolis.name, "Rio de Janeiro")
        self.assertEqual(metropolis.state_id, "0132-7890-6803")

    def test_create_update_City(self):
        """This is a test that validate attribute value change in update.
        """
        metropolis = City()
        pop = metropolis.name = "Paris"
        metropolis.state_id = "613-29-5285"
        metropolis.save()
        pop2 = metropolis.name = "Beijing"
        metropolis.save()
        self.assertNotEqual(pop, pop2)
