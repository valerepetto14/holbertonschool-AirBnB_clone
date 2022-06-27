#!/usr/bin/python3
"""
TEST OF CLASS BASE
"""


import unittest
import json
from models.base_model import BaseModel


class test_base_model(unittest.TestCase):
    """def class Testbasemodel"""
    def test_id(self):
        """2 instancias deben tener diferente id"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertFalse(obj1.id == obj2.id)
    
    def test_date(self):
        """test date"""
        obj1 = BaseModel()
        self.assertEqual(obj1.created_at, obj1.updated_at)
    
    def test_save(self):
        """test save"""
        obj1 = BaseModel()
        obj1.save()
        self.assertNotEqual(obj1.created_at, obj1.updated_at)

    def test_dict(self):
        """comprobar typo del update luego de to_dict()"""
        obj1 = BaseModel()
        dic = obj1.to_dict()
        self.assertEqual(type(dic["updated_at"]), str)
        self.assertEqual(type(dic["created_at"]), str)



    # def test_print(self)
    #     """test"""
    #     self.assertEqual(BaseModel(1), self.id == 1)
    #     self.assertEqual(BaseModel(1000), self.id == 1000)
    #     self.assertEqual(BaseModel(3), self.id == 3)

