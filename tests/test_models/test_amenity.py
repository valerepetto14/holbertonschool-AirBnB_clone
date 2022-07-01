#!/usr/bin/python3
"""
TEST OF CLASS AMENITY
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel
from models.amenity import Amenity

class test_amenity(unittest.TestCase):
    """Casos de prueba para la clase Amenity"""
    def test_instances_attr(self):
        """chequeamos attr(type, value) y confirmamos procedencia"""
        obj = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertEqual(obj.name, "")
        self.assertEqual(type(obj.name), str)

if __name__ == '__main__':
  unittest.main()