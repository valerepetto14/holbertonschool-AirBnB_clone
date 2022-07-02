#!/usr/bin/python3
"""
TEST OF CLASS REVIEW
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel
from models.review import Review


class test_Review(unittest.TestCase):
    """Test to Review class"""
    def test_procedence(self):
        """chequeamos si efectivamente es una subclase"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instances(self):
        """chequeamos existencia de atributos"""
        obj = Review()
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.text, "")
        self.assertEqual(obj.user_id, "")

    def test_attributes(self):
        """test attributes existence"""
        obj = Review()
        self.assertTrue(hasattr(obj, 'place_id'))
        self.assertTrue(hasattr(obj, 'text'))
        self.assertTrue(hasattr(obj, 'user_id'))

    def test_attr_type(self):
        """test tipo de los atributos"""
        obj = Review()
        obj.place_id = "d1"
        obj.user_id = "123"
        obj.text = "muy lindo"

        self.assertEqual(type(obj.place_id), str)
        self.assertEqual(type(obj.user_id), str)
        self.assertEqual(type(obj.text), str)

    def test_dif_id(self):
        """chequeamos la creación de distintos id"""
        obj = Review()
        other = Review()
        self.assertNotEqual(obj.id, other.id)

    def test_with_args(self):
        """chequeamos creación de atributos"""
        obj = Review()
        obj.place_id = "aldea"
        obj.text = "muy agradable"
        obj.user_id = "12df"
        self.assertEqual(obj.place_id, "aldea")
        self.assertEqual(obj.text, "muy agradable")
        self.assertEqual(obj.user_id, "12df")


if __name__ == '__main__':
    unittest.main()
