"""
Clase State:
    - hereda de BaseModel.
Public class attributes:
    -name: string - empty string
"""
from models.base_model import BaseModel
import models
from uuid import uuid4
from datetime import datetime

class State(BaseModel):
    """Clase State
        - atributo publico de clase
    """
    name = ""