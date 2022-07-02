#!/usr/bin/python3
"""
TEST OF CLASS STATE
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel
from models.state import State

class test_State():
    """Test State class"""
    def test_attr(self):
        """test existencia atributo"""
        obj = State()
        obj.name = ""
        self.assertTrue(hasattr(obj, "name"))
        self.assertEqual(obj.name, "")

    def test_type_attr(self):
        """test type de atributo"""
        obj = State()
        obj.name = "santi"
        self.assertEqual(type(obj.name), str)

    def test_instantiation(self):
        """Chequeamos la instancia con y sin argumentos"""
        self.assertIs(State, type(State(name="Naruto")))
        self.assertIs(State, type(State()))
        
    def test_save_updated(self):
        """funcionamiento del updated"""
        obj = State()
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_json(self):
        """Chequeamos inst al usar llamar save to json"""
        obj = State()
        obj.save()
        self.assertIs(type(obj.to_dict()), dict)


if __name__ == '__main__':
  unittest.main()