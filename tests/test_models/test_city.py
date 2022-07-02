#!/usr/bin/python3
"""
TEST OF CLASS CITY
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel
from models.city import City


class test_City(unittest.TestCase):
    """test to class City"""
    def test_procedence(self):
        """chequeamos que sea una subclase de basemodel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attr_type(self):
        """chequeamos tipo de atributos"""
        obj = City()
        self.assertEqual(type(obj.name), str)
        self.assertEqual(type(obj.state_id), str)

    def tests_instances_attr(self):
        """chequeamos attr(type, value), subclass"""
        self.assertTrue('state_id' in City.__dict__)
        self.assertTrue('name' in City.__dict__)

    def test_str(self):
        """Tests para str"""
        obj = City()
        string = f"[City] ({obj.id}) {obj.__dict__}"
        self.assertEqual(string, str(obj))

    def test_save(self):
        """Chequeamos el save"""
        obj = City()
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)


if __name__ == '__main__':
    unittest.main()
