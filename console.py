#!/usr/bin/python3
"""
Class console command that opens cmd interface to edit and update files
"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = ":) "

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
