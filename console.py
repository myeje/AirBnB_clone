#!/usr/bin/python3
"""
Class console command that opens cmd interface to edit and update files
"""
import cmd
from models import storage
from models.engine.file_storage import FileStorage
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

    def help_create(self):
        """
        Display the help for the create command.
        """
        print("Create a new instance of a specified"
              "class and save it to a JSON file")

    def do_show(self, args):
        """
        Display the string representation of an instance.
        Usage: show User <id>
        """
        if not args:
            print(f"** class name missing **")
            return
        arg = args.split()
        if arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print(f"** instance id missing **")
            return
        storage = FileStorage()
        obj_dict = storage.all()
        obj_key = f"{arg[0]}.{arg[1]}"
        if obj_key not in obj_dict:
            print("** no instance found **")
            return
        print(obj_dict[obj_key])
        if act == "show":
            print(obj_dict[obj_key])
        elif act == "destroy":
            del obj_dict[obj_key]
            storage.save()

    def help_show(self):
        """
        Display help for the show command.
        """
        print("Display the string representation of an instance")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy User <id>
        """
        self._validate_destroy(args, "destroy")

    def help_destroy(self):
        """
        Display help for the destroy command.
        """
        print("Delete an instance based on the class name and id")

    def do_all(self, args):
        """
        Display string representation of all instance or all instance
        of a specific class.
        Usage: all[class_name]
        """
        storage = FileStorage()
        obj_dict = storage.all()
        if not args:
            for obj_key, obj in obj_dict.items():
                print(obj)
        elif args in self.classes:
            for obj_key, obj in obj_dict.items():
                if obj_key.split('.')[0] == args:
                    print(obj)
        else:
            print("** class doesn't exist **")

    def help_all(self):
        """
        Display help for all command
        """
        print("Display string representations of all instances,"
              "or all instances of a specific class")
        print("Usage: all[class_name]")

    def do_update(self, args):
        """
        Update an instance based on the class name and id.
        Usage: update User <id> <attribute name> "<attribute value>"
        """
        self._validate_update(args)

    def help_update(self):
        """
        Display help for the update command.
        """
        print("Update an instance based on the class name and id")

    def _validate_destroy(self, args, act):
        if not args:
            print(f"** class name missing **")
            return
        arg = args.split()
        if arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print(f"** instance id missing **")
            return
        storage = FileStorage()
        obj_dict = storage.all()
        obj_key = f"{arg[0]}.{arg[1]}"
        if obj_key not in obj_dict:
            print("** no instance found **")
            return
        if act == "show":
            print(obj_dict[obj_key])
        elif act == "destroy":
            del obj_dict[obj_key]
            storage.save()

    def _validate_update(self, args):
        if not args:
            print("** class name missing **")
            return
        arg = args.split()
        if arg[0] not in self.classes:
            print("** class doesn't  exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        storage = FileStorage()
        obj_dict = storage.all()
        obj_key = f"{arg[0]}.{arg[1]}"
        if obj_key not in obj_dict:
            print("** no instance found **")
            return
        if len(arg) < 3:
            print("** attribute name missing **")
            return
        if len(arg) < 4:
            print("** value missing **")
            return
        instance = obj_dict[obj_key]
        setattr(instance, args[2], args[3])
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
