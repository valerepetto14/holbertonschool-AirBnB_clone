#!/usr/bin/python3
"""
programm console
"""
from models.base_model import BaseModel
import json
import cmd


class HBNBCommand(cmd.Cmd):
    """def class cmd"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """def exit"""
        exit()

    def do_EOF(self, line):
        """def EOF"""
        exit()

    def do_emptyline(self):
        """linea vacia no hacemos nada"""
        pass

    def do_create(self, line):
        """create a new instance of BaseModel"""
        class_val = ["BaseModel"]
        args = line.split()
        if line == "" or line is None or len(args) < 1:
            print("** class name missing **")
            return
        clase = args[0]
        if clase not in class_val:
            print("** class doesn't exist **")
            return
        """
        evalua como código una cadena
        si el comando existe lo ejecuto
        """
        if clase in class_val:
            obj = eval(clase)()
            """saves it (to the JSON file) and prints the id"""
            obj.save()
            print(obj.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
