#!/usr/bin/python3
"""
Class FileStorage:
- serializa las Instancias en un 'archivo' JSON
- deserializa el 'archivo' JSON a Instancias
"""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    serializar a un archivo/deserializar de un archivo
    """
    def __init__(self):
        """initialize"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """return all the objects"""
        return self.__objects

    def new(self, obj):
        """method new sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """pasar el diccionario recibido a JSON string"""
        dic = {}
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            for key, value in self.__objects.items():
                dic[key] = value.to_dict()
            json.dump(dic, f, indent=4)

    def reload(self):
        """
        deserializes the JSON file to /
        (only if the JSON file (__file_path) exists, otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, mode="r") as f:
                dic = json.load(f)
            for key, value in dic.items():
                self.__objects[key] = eval(value["__class__"])(**value)
        else:
            pass
