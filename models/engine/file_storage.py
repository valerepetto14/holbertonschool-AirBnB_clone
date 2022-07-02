#!/usr/bin/python3
"""
Module for creating a class: FileStorage
"""
from models.base_model import BaseModel
import json
from os.path import exists
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    Class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances.
    """
    # Private class attributes:
    __file_path = "file.json"  # string - path to the JSON file
    __objects = {}

    # Public instance methods:
    def all(self):
        """
        Returns the dictionary __objects that contains all the objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in priv attribute __objects the obj with key <obj class name>.id
        Add a new object in the current dict with format: <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        aux_dict = {}
        # cargar el aux_dict con la info que este en objects
        # se serializa cada objeto que esta en __objects
        for key, value in self.__objects.items():
            aux_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as json_file:
            json.dump(aux_dict, json_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised).
        """
        if exists(self.__file_path) is True:
            with open(self.__file_path, mode="r", encoding="UTF-8") as f:
                aux_dict2 = json.load(f)
            for key, value in aux_dict2.items():
                self.__objects[key] = eval(value["__class__"])(**value)
        #  estas ejecutando lo que devuelve el eval que es el nombre de
        #  la clase y a eso le pasas como parametro (**value)
        else:
            pass