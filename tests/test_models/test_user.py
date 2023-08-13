#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User
"""
This is a unittest for class User
"""


class TestUser(unittest.TestCase):
    """Testing unittest"""
    def test_validate_format(self):
        """This is a test that validate the format that is string
        """
        client = User()
        self.assertIsInstance(client.email, str)
        self.assertIsInstance(client.password, str)
        self.assertIsInstance(client.first_name, str)
        self.assertIsInstance(client.last_name, str)

    def test_User_is_Subclass(self):
        """This is a test for BaseModel subclasses
        """
        client = User()
        pop = client.__class__
        self.assertTrue(issubclass(pop, BaseModel))

    def test_empty_string(self):
        """This is test that validate if it is empty.
        """
        client = User()
        self.assertEqual(client.email, "")
        self.assertEqual(client.password, "")
        self.assertEqual(client.first_name, "")
        self.assertEqual(client.last_name, "")

    def test_representation_user(self):
        """This is a test that validate the representation of the User.
        """
        client = User()
        pop = client.__dict__
        lop = "[{}] ({}) {}".format(client.__class__.__name__,
                                                      client.id, pop)
        self.assertEqual(lop, str(client))

    def test_create_User(self):
        """This is a test that validate user creation.
        """
        client = User()
        client.email = "deosundeola12@gmail.com"
        client.password = "12345"
        client.first_name = "Oluwaseyi"
        client.last_name = "Adeosun"
        client.save()
        self.assertEqual(client.email, "deosundeola12@gmail.com")
        self.assertEqual(client.password, "12345")
        self.assertEqual(client.first_name, "Oluwaseyi")
        self.assertEqual(client.last_name, "Adeosun")

    def test_create_update_User(self):
        """This is a test that validate attribute value change in update.
        """
        client = User()
        client.email = "ehimareemore67@gmail.com"
        pop = client.password = "56789"
        client.first_name = "Joshua"
        client.last_name = "Emore"
        update2 = client.updated_at
        client.save()
        pop2 = client.password = "123345"
        update1 = client.updated_at
        client.save()
        self.assertNotEqual(pop, pop2)
        self.assertNotEqual(update1, update2)
