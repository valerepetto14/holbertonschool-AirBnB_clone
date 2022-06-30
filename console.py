#!/usr/bin/python3
"""
programm console
"""
import models
from models.base_model import BaseModel
# from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import cmd
import os


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

    def do_show(self, line):
        """mostra dict de un Base model con id pasado"""
        base = models.storage.all()
        class_val = ["BaseModel"]
        flag = 0
        args = line.split()
        if line == "" or line is None or len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in class_val:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        else:
            for key, value in base.items():
                key_split = key.split('.')
                if(key_split[0] == args[0] and key_split[1] == args[1]):
                    print(value)
                    flag = 1
            if flag == 0:
                print("** no instance found **")

    def do_destroy(self, line):
        base = models.storage.all()
        """mostra dict de un Base model con id pasado"""
        class_val = ["BaseModel"]
        flag = 0
        args = line.split()
        if line == "" or line is None or len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in class_val:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if os.path.exists('file.json') is True:
            base_copy = base.copy()
            for key, value in base_copy.items():
                key_split = key.split('.')
                if(key_split[0] == args[0] and key_split[1] == args[1]):
                    del base[key]
                    models.storage.save()
                    flag = 1
                if flag == 0:
                    print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not
        on the class name, "all" and "all class_name"
        """
        base = models.storage.all()
        class_val = ["BaseModel"]
        args = line.split()
        if line == "" or line is None or len(args) < 1:
            """
            debe funcionar sin importar si tiene
            nombre de clase o no"""
            lista_aux = []
            for key, value in base.items():
                lista_aux.append(f"{value}")
            print(lista_aux)
            return
        if args[0] not in class_val:
            print("** class doesn't exist **")
            return
        lista_ins = []
        if args[0] in class_val:
            for key, value in base.items():
                key_split = key.split('.')
                if(key_split[0] == args[0]):
                    lista_ins.append(f"{value}")
                print(lista_ins)
        else:
            pass

    def do_update(self, line):
        """
        update attributes
        """
        class_val = ["BaseModel", "User"]
        args = line.split()
        if line == "" or line is None or len(args) < 1:
            print("** class name missing **")
        if args[0] not in class_val:
            print("** class doesn't exist **")
        if len(args) == 1:
            print("** instance id missing **")
        if len(args) == 2:
            print("** attribute name missing **")
        if len(args) == 3:
            print("** value missing **")
        if (len == 4):
            base = models.storage.all()
            base_cp = base.copy()
            for key, value in base.items():
                key_split = key.split('.')
                if(key_split[0] == args[0] and key_split[1] == args[1]):
                    base_cp[key][args[2]] = args[3]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
