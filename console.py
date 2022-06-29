#!/usr/bin/python3
"""
programm console
"""

from models.base_model import BaseModel
import json
import cmd


class HBNBCommand(cmd.Cmd):
    """def class cmd"""

    prompt = '(hbnb)'
    def do_quit(self, line):
        """def exit"""
        exit()

    def do_EOF(self, line):
        """def EOF"""
        exit()

    def do_create(self, line):
        """def create"""
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()