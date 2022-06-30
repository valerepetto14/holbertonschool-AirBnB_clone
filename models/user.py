"""
Clase User:
    - hereda de BaseModel.
Public class attributes:
    -email: string - empty string
    -password: string - empty string
    -first_name: string - empty string
    -last_name: string - empty string
"""
import models
from uuid import uuid4
from datetime import datetime

class User(BaseModel):
    """Clase User Heredada de BaseModel
        - atributos de clase publicos
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
