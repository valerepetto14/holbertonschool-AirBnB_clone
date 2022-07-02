#!/usr/bin/python3
"""The console or Command Interpreter"""

import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class that we use to generate the console"""

    prompt = "(hbnb) "
    clases = ["BaseModel", "City", "Amenity",
              "Place", "Review", "State", "User"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit()

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        sys.exit()

    def emptyline(self):
        """Do nothing"""
        pass

    def do_create(self, arg):
        """Command used to create a new object."""
        if len(arg) < 1:
            print("** class name missing **")
        else:
            args = arg.split()[0]
            if args in self.clases:
                new_ins = eval(args)()
                new_ins.save()
                print(new_ins.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Command used to show the information of an object."""
        if len(arg) < 1:
            print("** class name missing **")
        else:
            args = arg.split()
            if len(args) == 1:
                if args[0] not in self.clases:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            else:
                if args[0] not in self.clases:
                    print("** class doesn't exist **")
                else:
                    object = f"{args[0]}.{args[1]}"
                    aux_dictionary = models.storage.all()
                    if object in aux_dictionary:
                        print(aux_dictionary[object])
                    else:
                        print("** no instance found **")

    def do_destroy(self, arg):
        """Command used to deletes an object."""
        if len(arg) < 1:
            print("** class name missing **")
        else:
            args = arg.split()
            if len(args) == 1:
                if args[0] not in self.clases:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            else:
                if args[0] not in self.clases:
                    print("** class doesn't exist **")
                else:
                    object = f"{args[0]}.{args[1]}"
                    aux_dictionary = models.storage.all()
                    if object in aux_dictionary:
                        del aux_dictionary[object]
                        models.storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, arg):
        """Command used to print all created objects."""
        array = []
        args = arg.split()
        if len(arg) >= 1:
            if args[0] in self.clases:
                aux_dictionary = models.storage.all()
                for key, value in aux_dictionary.items():
                    if key.split(".")[0] == args[0]:
                        string = str(value)
                        array.append(string)
                print(array)
            else:
                print("** class doesn't exist **")
        else:
            aux_dictionary = models.storage.all()
            for key, value in aux_dictionary.items():
                string = str(value)
                array.append(string)
            print(array)

    def do_update(self, arg):
        """Command used to uptdate attributes from created obejects"""
        args = arg.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif args[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            object = f"{args[0]}.{args[1]}"
            aux_dictionary = models.storage.all()
            if object not in aux_dictionary:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                object = aux_dictionary.get(object)
                setattr(object, args[2], args[3])
                models.storage.save()

    def do_count(self, arg):
        """Show the cuantity of an specified instance"""
        counter = 0
        if arg in self.clases:
            for key, objects in models.storage.all().items():
                if arg in key:
                    counter += 1
            print(counter)
        else:
            print("** class doesn't exist **")

    def default(self, arg):
        """asd asd asd"""
        args = arg.split(".")
        my_class = args[0]
        command = args[1]

        if command == "all()":
            HBNBCommand.do_all(self, my_class)
        elif command == "count()":
            HBNBCommand.do_count(self, my_class)
        elif command[0:4] == "show":
            id = args[1].split("(")[1]
            id = id.split(")")[0]
            arg = my_class + " " + id
            HBNBCommand.do_show(self, arg)
        elif command[0:7] == "destroy":
            id = args[1].split("(")[1]
            id = id.split(")")[0]
            arg = my_class + " " + id
            HBNBCommand.do_destroy(self, arg)
        elif command[0:6] == "update":
            id = args[1].split("(")[1]
            id = id.split(",")[0]

            arg1 = args[1].split("(")[1]
            arg1 = arg1.split(",")[1]
            arg1 = arg1.split(" ")[1]

            arg2 = args[1].split("(")[1]
            arg2 = arg2.split(",")[2]
            arg2 = arg2.split(")")[0]

            arg = my_class + " " + id + " " + arg1 + " " + arg2
            HBNBCommand.do_update(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()