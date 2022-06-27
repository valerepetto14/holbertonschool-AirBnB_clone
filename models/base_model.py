#!/usr/bin/python3
"""
Clase base:
- vamos a definir todos los atributos/metodos comunes
- de las que van a heredar distintas clases
"""
from uuid import uuid4


class BaseModel:
    """
    clase base para todos los modelos(objects)
    """
    def __init__(self):
        self.id = str(uuid4)

