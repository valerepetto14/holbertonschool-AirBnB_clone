#!/usr/bin/python3
"""
programm console
"""
from itertools import count
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.review import Review
from models.state import State
from models.place import Place
from models.amenity import Amenity
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

    def emptyline(self):
        """linea vacia no hacemos nada"""
        pass

    def do_create(self, line):
        """create a new instance of BaseModel"""
        class_val = ["BaseModel", "User", "State", "City", "Amenity",
                     "Place", "Review"]
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
        class_val = ["BaseModel", "User", "State", "City", "Amenity",
                     "Place", "Review"]
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
        class_val = ["BaseModel", "User", "State", "City", "Amenity",
                     "Place", "Review"]
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
        class_val = ["BaseModel", "User", "State", "City", "Amenity",
                     "Place", "Review"]
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
        if args[0] in class_val:
            lista_ins = []
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
        class_val = ["BaseModel", "User", "State", "City", "Amenity",
                     "Place", "Review"]
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
        if len(args) == 4:
            base = models.storage.all()
            for key, value in base.items():
                key_split = key.split('.')
                if(key_split[0] == args[0] and key_split[1] == args[1]):
                    setattr(value, args[2], args[3])
                    models.storage.save()
                    # objeto = dir(value)
                    # if args[2] in objeto:
                    #     setattr(value,args[2],args[3])
                    #     models.storage.save()
                    # else:
                    #     setattr(value,args[2],args[3])
                    #     models.storage.save()

    def do_count(self, arg):
        """contar el numero de instancias de una clase"""
        class_val = ["BaseModel", "User", "State", "City", "Amenity",
                     "Place", "Review"]
        base = models.storage.all()
        count = 0
        if arg in class_val:
            for key, value in base.items():
                key_split = key.split('.')
                if key_split[0] == arg:
                    count += 1
            print(count)

    def default(self, line):
        base = models.storage.all()
        class_val = ["BaseModel", "User", "State", "City", "Amenity"]
        comando = line.split(".")
        lista_ins = []
        if comando[0] in class_val and comando[1] == "all()":
            HBNBCommand.do_all(self, comando[0])
        elif comando[0] in class_val and comando[1] == "count()":
            HBNBCommand.do_count(self, comando[0])
        elif comando[0] in class_val and "show" in comando[1]:
            ide = comando[1].split('(')
            ide1 = ide[1].split(')')
            print(f"{comando[0]}{ide1[0]}")
            HBNBCommand.do_show(self, f"{comando[0]} {ide1[0]}")
        else:
            print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
