#!/usr/bin/python3
"""
Class console command that opens cmd interface to edit and update files
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]
    valid_commands = ["all", "count"]

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """EOF command to exit the program (CTRL + D)"""
        return True

    def emptyline(self):
        """Override emptyline to do nothing"""
        return False

    def help_quit(self):
        """
        Display help for the quit command.
        """
        print("Quit the command to exit the program\n")

    def help_EOF(self):
        """
        Display help for the EOF command.
        """
        print("Exit the command interpreter using EOF (Ctrl+D)\n")

    def help_help(self):
        """
        Display help for the help command
        """
        print("Show help for the available commands\n")

    def do_create(self, args):
        """
        Create a new instance of User and saves it to a JSON file.
        Usage: create User.
        """
        if not args:
            print("** class name missing **")
            return
        arg = args.split()
        if arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        new = eval(arg[0])()
        new.save()
        print(new.id)

    def do_show(self, args):
        """
        Display the string representation of an instance.
        Usage: show User <id>
        """
        self._validate_show_and_destroy(arg, "destroy")

    def do_destroy(Self, args):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy User <id>
        """
        self._validate_show_and_destroy(args, "destroy")

    def do_update(self, args):
        """
        Update an instance based on the class name and id.
        Usage: update User <id> <attribute name> "<attribute value>"
        """
        self._validate_update(args)

    def _validate_show_and_destroy(self, arg, 
