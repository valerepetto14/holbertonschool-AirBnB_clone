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
    def __init__(self, *args, **kwargs)
        """initialization"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
        # if kwargs is not None and len(kwargs):
        #     print(print("{} - {}".format(args, kwargs)))

    def __str__(self):
        """
        return a string representationddd
        """
        return (f"[{__class__}] ({self.id}) {self.__dict__}")

    def save(self):
        """method save"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return a dictionary with methods/attr"""
        diccio = self.__dict__.copy()
        diccio["__class__"] = BaseModel.__name__
        diccio["updated_at"] = self.updated_at.isoformat()
        diccio["created_at"] = self.updated_at.isoformat()
        return diccio
