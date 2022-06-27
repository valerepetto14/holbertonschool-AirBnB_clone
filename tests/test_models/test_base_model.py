#!/usr/bin/python3
"""
TEST OF CLASS BASE
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel


class test_base_model(unittest.TestCase):
    """def class Testbasemodel"""
    def test_instancias(self):
        """checkear si se crearon las instancias"""
        obj1 = BaseModel()
        self.assertTrue(hasattr(obj1, "id"))
        self.assertTrue(hasattr(obj1, "created_at"))
        self.assertTrue(hasattr(obj1, "updated_at"))

    def test_id(self):
        """2 instancias deben tener diferente id"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertFalse(obj1.id == obj2.id)
    
    def test_data_dif(self):
        """crear 2 instancias en diferentes tiempos"""
        obj1 = BaseModel()
        sleep(0.1)
        obj2 = BaseModel()
        self.assertNotEqual(obj1.created_at, obj2.created_at)

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

    def test_kwarg(self):
        """test que valida que se llene mediante un diccionario"""
        dic = {'id':'12','created_at': '2017-09-28T21:03:54.052302','updated_at': '2017-09-28T21:03:54.052302'}
        obj1 = BaseModel(**dic)
        self.assertEqual(obj1.id, "12")
        self.assertEqual(obj1.created_at, datetime.strptime('2017-09-28T21:03:54.052302', '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(obj1.updated_at, datetime.strptime('2017-09-28T21:03:54.052302', '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(type(dic["created_at"]), str)
    
    # def test_no_kwarg
        

    # def test_print(self)
    #     """test"""
    #     self.assertEqual(BaseModel(1), self.id == 1)
    #     self.assertEqual(BaseModel(1000), self.id == 1000)
    #     self.assertEqual(BaseModel(3), self.id == 3)

