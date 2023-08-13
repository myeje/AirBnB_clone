#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.state import State
"""
This is a unittest for class State
"""


class TestState(unittest.TestCase):
    """Testing unittest"""
    def test_validate_format(self):
        """This is a test that validate format that is string.
        """
        region = State()
        self.assertIsInstance(region.name, str)

    def test_State_is_Subclass(self):
        """This is a test for BaseModel subclasses.
        """
        region = State()
        pop = region.__class__
        self.assertTrue(issubclass(pop, BaseModel))

    def test_empty_string(self):
        """This is a test that validate if it is empty.
        """
        region = State()
        self.assertEqual(region.name, "")

    def test_representation_state(self):
        """This is a test that validate the representation of the User.
        """
        region = State()
        pop = region.__dict__
        lop = "[{}] ({}) {}".format(
                region.__class__.__name__,region.id, pop)
        self.assertEqual(lop, str(region))

    def test_create_State(self):
        """This is a test that validate user creation.
        """
        region = State()
        region.name = "Arizona"
        self.assertEqual(region.name, "Arizona")

    def test_create_update_State(self):
        """This is a test that validate attribute value change in update.
        """
        region = State()
        pop = region.name = "Texas"
        region.save()
        pop2 = region.name = "California"
        region.save()
        self.assertNotEqual(pop, pop2)
