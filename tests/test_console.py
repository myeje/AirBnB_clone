#!/usr/bin/python3
import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
from io import StringIO
from unittest.mock import patch
from models.engine.file_storage import FileStorage
"""
Unittest for Console
"""


class TestConsole(unittest.TestCase):

    def setUp(self):
        """
        Set up test fixture
        """
        self.console = HBNBCommand()
        self.user = User()
        self.user.name = "John Doe"
        self.user.save()

    def tearDown(self):
        """
        Tear down test fixture
        """
        try:
            storage.clear()
        except Exception as e:
            print(e)

    def test_create(self):
        """
        Test the create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue()
            self.assertEqual(output, "1\n")

    def test_show(self):
        """
        Test the show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User 1")
            output = f.getvalue()
            self.assertEqual(output, "John Doe\n")

    def test_destroy(self):
        """
        Test the destroy command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User 1")
            output = f.getvalue()
            self.assertEqual(output, "1\n")

    def test_all(self):
        """
        Test the all command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue()
            self.assertIn("User", output)
            self.assertIn("1", output)

    def test_update(self):
        """
        Test the update command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User 1 name David Doe")
            output = f.getvalue()
            self.assertEqual(output, "1\n")

            self.user = User.objects.get(id=1)
            self.assertEqual(self.user.name, "David Doe")

    def test_count(self):
        """
        Test the count command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count User")
            output = f.getvalue()
            self.assertEqual(output, "1\n")

    def test_help(self):
        """
        Test the help command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue()
            self.assertIn("create", output)
            self.assertIn("show", output)
            self.assertIn("destroy", output)
            self.assertIn("all", output)
            self.assertIn("update", output)
            self.assertIn("count", output)
            self.assertIn("quit", output)
