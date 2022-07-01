"""
Clase Amenity:
    - hereda de BaseModel.
Public class attributes:
    -name: string - empty string
"""
from models.base_model import BaseModel
import models
from uuid import uuid4
from datetime import datetime


class Amenity(BaseModel):
    """Clase Amenity
    - Public class attribute
    """
    name = ""
