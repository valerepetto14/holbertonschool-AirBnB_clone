#!/usr/bin/python3
"""
Clase base:
- vamos a definir todos los atributos/metodos comunes
- de las que van a heredar distintas sub_clases
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    clase base para todos los modelos
    """
    def __init__(self, *args, **kwargs):
        """initialization"""
        # print(kwargs)
        if (kwargs is not None and len(kwargs) != 0):
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == 'id':
                    self.id = value
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        return a string representationddd
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """method save"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dictionary with methods/attr"""
        diccio = self.__dict__.copy()
        diccio["__class__"] = self.__class__.__name__
        diccio["updated_at"] = self.updated_at.isoformat()
        diccio["created_at"] = self.updated_at.isoformat()
        return diccio
