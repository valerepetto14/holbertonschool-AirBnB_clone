#!/usr/bin/python3
"""
Module for creating a base class: BaseModel
"""
from uuid import uuid4
from datetime import datetime
import models  # if we put: from models import storage -> error:circular import


class BaseModel:
    """class base"""
    def __init__(self, *args, **kwargs):
        """
        Initialize an instance of BaseModel with the following
        Public instance attributes:
        id: string - assign with an uuid when an instance is created:
        you can use uuid.uuid4() to generate unique id.
        created_at: datetime - assign with the current datetime when an
        instance is created
        updated_at: datetime - assign with the current datetime when an
        instance is created and it will be updated every time you change
        your object
        """
        if kwargs and kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                elif key == "__class__":
                    pass  # No le seteamos nada,solo usamos pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())  # convert the id to string
            self.created_at = datetime.now()  # Use method now of datetime mod
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        instance.
        __dict__ is a pecial attribute of every module, is the dictionary
        containing the module’s symbol table.
        - Usamos la funcion "getattr", a la misma se le pasa la instancia
        correspondiente (con self) y el attribute del cual se quiere
        obtener el valor.
        """

        new_dict = {}

        for attribute in self.__dict__:
            if attribute == "created_at" or attribute == "updated_at":
                new_dict[attribute] = getattr(self, attribute).isoformat()
            else:
                new_dict[attribute] = getattr(self, attribute)
        new_dict['__class__'] = self.__class__.__name__
        # Se agrega la key: "__class__" y se le asigna el nombre de la clase.
        return (new_dict)