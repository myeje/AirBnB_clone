#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review
"""
This is a unittest for class Review
"""


class TestReview(unittest.TestCase):
    """Testing unittest"""
    def test_validate_format(self):
        """This is a test that validate the format that is string
        """
        examine = Review()
        self.assertIsInstance(examine.place_id, str)
        self.assertIsInstance(examine.user_id, str)
        self.assertIsInstance(examine.text, str)

    def test_review_is_Subclass(self):
        """This is a test for BaseModel subclasses
        """
        examine = Review()
        pop = examine.__class__
        self.assertTrue(issubclass(pop, BaseModel))

    def test_empty_string(self):
        """This is a test that validate if it is empty.
        """
        examine = Review()
        self.assertEqual(examine.place_id, "")
        self.assertEqual(examine.user_id, "")
        self.assertEqual(examine.text, "")

    def test_representation_review(self):
        """This is a test to validate the  representation of the User.
        """
        examine = Review()
        pop = examine.__dict__
        lop = "[{}] ({}) {}".format(
                examine.__class__.__name__, examine.id, pop)
        self.assertEqual(lop, str(examine))

    def test_create_Review(self):
        """This is a test that validate user creation
        """
        examine = Review()
        examine.place_id = "Ch7fuy7u-hs7t-djte67udy"
        examine.user_id = "lovebug"
        examine.text = "Stunning place"
        self.assertEqual(examine.place_id, "Ch7fuy7u-hs7t-djte67udy")
        self.assertEqual(examine.user_id, "lovebug")
        self.assertEqual(examine.text, "Stunning place")

    def test_create_update_Review(self):
        """Test that validate attribute value change in update.
        """
        examine = Review()
        examine.place_id = "Ch7fuy7u-hs7t-djte67udy"
        examine.name = "Grace"
        pop = examine.text = "Great experience"
        examine.save()
        pop2 = examine.text = "Worst experience"
        examine.save()
        self.assertNotEqual(pop, pop2)
