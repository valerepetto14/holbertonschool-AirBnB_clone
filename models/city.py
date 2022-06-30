"""
Clase City:
    - hereda de BaseModel.
Public class attributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
"""
from models.base_model import BaseModel
import models
from uuid import uuid4
from datetime import datetime


class City(BaseModel):
    """Clase City
        -Atributos publicos de clase
    """
    state_id = State.id # ???
    name = ""