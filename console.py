#!/usr/bin/python3
"""creating the command interpreter"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class HBNBCommand(cmd.Cmd):
    """
    the console
    """
    prompt = "(hbnb) "

    __cls = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
        ]

    def emptyline(self):
        """Override emptyline to do nothing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program (CTRL + D)
        """
        print()
        return True

    def help_quit(self):
        """
        Display help for the quit command.
        """
        print("Quit command used to exit the program\n")
        print()

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

    def do_create(self, mode):
        """
        Create a new instance of User and saves it to a JSON file.
        Usage: create User.
        """
        if mode == "":
            print("** class name missing **")
        elif mode not in self.__cls:
            print("** class doesn't exist **")
        else:
            new = eval(mode)()
            new.save()
            print(new.id)

    def help_create(self):
        """
        Display the help for the create command.
        """
        print("Create a new instance of a specified"
              "class and save it to a JSON file")

    def do_show(self, mode):
        """
        Display the string representation of an instance.
        Usage: show User <id>
        """
        args = mode.split(" ")
        if mode == '':
            print("** class name missing **")
        elif args[0] not in self.__cls:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            char = "{}.{}".format(args[0], args[1])
            if char not in obj_dict:
                print("** no instance found **")
            else:
                print("{}".format(obj_dict[char]))

    def help_show(self):
        """
        Display help for the show command.
        """
        print("Display the string representation of an instance")

    def do_destroy(self, mode):
        """removes an instance based on class
           name, ID and saves it to a json file"""
        args = mode.split(" ")
        if mode == '':
            print("** class name missing **")
        elif args[0] not in self.__cls:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            char = "{}.{}".format(args[0], args[1])
            if char not in obj_dict:
                print("** no instance found **")
            else:
                del (obj_dict[char])
                storage.save()

    def help_destroy(self):
        """
        Display help for the destroy command.
        """
        print("Delete an instance based on the class name and id")

    def do_all(self, mode):
        """
        methods that prints all string representations
        of all instances based or not on class name
        """
        m = []
        aldir = storage.all()
        if mode == "":
            for key, value in aldir.items():
                m.append(str(value))
            print(m)
        elif mode in self.__cls:
            for key, value in aldir.items():
                if value.__class__.__name__ == mode:
                    m.append(str(value))
            print(m)
        else:
            print("** class doesn't exist **")

    def help_all(self):
        """
        Display help for all command
        """
        print("Display string representations of all instances,"
              "or all instances of a specific class")
        print("Usage: all[class_name]")

    def do_update(self, mode):
        """
        methods to update an instance based on class name and
        id by adding or updating the attribute that saves the
        change in the json file
        """
        args = mode.split(" ")
        if mode == '':
            print("** class name missing **")
        elif args[0] not in self.__cls:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            char = "{}.{}".format(args[0], args[1])
            if char not in obj_dict:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                m = ["id", "created_at", "updated_at"]
                if args[2] not in m:
                    for key, value in obj_dict.items():
                        setattr(value, args[2], eval(args[3]))
                        value.save()

    def help_update(self):
        """
        Display help for the update command.
        """
        print("Update an instance based on the class name and id")

    def do_count(self, mode):
        """
        Instance counter according to class.
        """
        args = mode.split(" ")
        if mode not in self.__cls:
            print("** class doesn't exist **")
        else:
            m = []
            d_l = storage.all()
            for k, v in d_l.items():
                if args[0] in k:
                    m.append(v)
            print(len(m))

    def help_count(self):
        """
        Display help for count command.
        """
        print("Display an the number of instances of a class")

    def default(self, mode):
        """
        cmd method to validate when it does not
        recognize the prefix of the command.
        """
        args = mode.split(".")
        parse = args[1].split("(")
        parse_line = parse[1].split(")")
        new_line = parse_line[0].split(",")
        if args[0] in self.__cls:
            if args[1] == "all()":
                mode_cls = args[0]
                return self.do_all(mode_cls)
            elif args[1] == "count()":
                mode_cls = args[0]
                return self.do_count(mode_cls)
            elif args[1][0:4] == 'show':
                mode_cls = args[0] + " " + parse_line[0]
                return self.do_show(mode_cls)
            elif args[1][0:7] == 'destroy':
                mode_cls = args[0] + " " + parse_line[0]
                return self.do_destroy(mode_cls)
            elif args[1][0:6] == "update":
                mode_cls = (
                    args[0] + " " + new_line[0] + "" +
                    new_line[1] + "" + new_line[2]
                )
                return self.do_update(mode_cls)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
