#!/usr/bin/python3
"""
TEST OF CLASS USER
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel
from models.user import User

class test_User(unittest.TestCase):
    """Test to class User"""
    def test_instances(self):
        """ Test para las nuevas instancias creadas"""
        obj = User()
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name, "")
        self.assertEqual(obj.last_name, "")
        self.assertEqual(obj.email, "")

    def test_dif_id(self):
        """Test difrentes id para las instancias"""
        obj = User()
        other = User()
        self.assertNotEqual(obj.id, other.id)

    def test_str_representation(self):
        """Validamos el formato del str"""
        obj = User()
        clase = obj.__class__.__name__
        ide = obj.id
        cadena = f"[{clase}] ({ide}) {obj.__dict__}"
        self.assertEqual(str(obj), cadena)

if __name__ == '__main__':
  unittest.main()