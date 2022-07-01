"""
Clase Review:
    - hereda de BaseModel.
Public class attributes:
    -place_id: string - empty string: it will be the Place.id
    -user_id: string - empty string: it will be the User.id
    -text: string - empty string
"""
from models.base_model import BaseModel
import models
from uuid import uuid4
from datetime import datetime


class Review(BaseModel):
    """Clase Place
        -Atributos publicos de clase
    """
    place_id = ""
    user_id = ""
    text = ""
