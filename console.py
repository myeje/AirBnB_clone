#!/usr/bin/python3
"""
Class console command that opens cmd interface to edit and update files
"""
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = ":) \n"

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """EOF command to exit the program (CTRL + D)"""
        return True

    def emptyline(self):
        """Override emptyline to do nothing"""
        pass

    def do_create(self, model_type="None"):
        """
        Creates a new instance of BaseModel saves it
        (to the JSON file) and prints the id.
        """
        if not model_type:
            print("** class name missing **")
        elif model_type not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_model = eval(model_type)()
            new_model.save()
            print(new_model.id)


    def do_show(self, model_key=None):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        if not model_key:
            print("** class name missing **")
            return

        args = model_key.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        model_id = args[1]

        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        obj_key = f"{class_name}.{model_id}"
        obj = storage.all().get(obj_key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, model_key=None):
        """
        Deletes an instance based on the class name and id
        """
        if not model_key:
            print("** class name missing **")
            return

        args = model_key.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        model_id = args[1]

        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        obj_key = f"{class_name}.{model_id}"
        obj = storage.all().get(obj_key)
        if obj is None:
            print("** no instance found **")
        else:
            del storage.all()[obj_key]
            storage.save()

    def do_all(self, model_type=""):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """
        if model_type and model_type not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        ob = []
        for key, obj in storage.all().items():
            if not model_type or obj.__class__.__name__ == model_type:
                ob.append(str(obj))
                print(ob)

    def do_update(self, model_info):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        args = model_info.split()
        if len(args) < 3:
            print("** class name missing **")
            return

        class_name = args[0]
        model_id = args[1]
        attribute_name = args[2]

        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 4:
            print("** instance id missing **")
            return

        if len(args) < 5:
            print("** attribute name missing **")
            return

        if len(args) < 6:
            print("** value missing **")
            return

        obj_key = f"{class_name}.{model_id}"
        obj = storage.all().get(obj_key)
        if obj is None:
            print("** no instance found **")
        else:
            attribute_value = " ".join(args[3:])
            setattr(obj, attribute_name, attribute_value)
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
