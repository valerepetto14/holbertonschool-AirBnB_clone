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
    def __init__(self):
        """initialization"""
        self.id = str(uuid4)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
