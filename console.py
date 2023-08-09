#!/usr/bin/python3
"""
Class console command that opens cmd interface to edit and update files
"""
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = ":) "

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            instances = storage.all()
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")
        except IndexError:
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            instances = storage.all()
            if key in instances:
                instances.pop(key)
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        instances = storage.all()
        if not arg:
            print([str(instance) for instance in instances.values()])
        else:
            try:
                class_name = arg
                if class_name in BaseModel.__subclasses__():
                    class_instances = [str(instance) for key, instance in instances.items() if class_name in key]
                    print(class_instances)
                else:
                    print("** class doesn't exist **")
            except IndexError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            instances = storage.all()
            if key not in instances:
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return

            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return

            value = args[3]
            instance = instances[key]
            setattr(instance, attribute_name, value)
            instance.save()
        except IndexError:
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
