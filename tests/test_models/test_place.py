#!/usr/bin/python3
"""
TEST OF CLASS PLACE
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel
from models.place import Place


class test_Place(unittest.TestCase):
    """test Place"""
    def test_procedence(self):
        """chequeamos si efectivamente es una subclase"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attr(self):
        """test existencia de atributos"""
        obj = Place()
        self.assertTrue(hasattr(obj, "city_id"))
        self.assertTrue(hasattr(obj, "user_id"))
        self.assertTrue(hasattr(obj, "name"))
        self.assertTrue(hasattr(obj, "description"))
        self.assertTrue(hasattr(obj, "number_rooms"))
        self.assertTrue(hasattr(obj, "number_bathrooms"))
        self.assertTrue(hasattr(obj, "max_guest"))
        self.assertTrue(hasattr(obj, "price_by_night"))
        self.assertTrue(hasattr(obj, "latitude"))
        self.assertTrue(hasattr(obj, "longitude"))
        self.assertTrue(hasattr(obj, "amenity_ids"))
        self.assertTrue(issubclass(Place, BaseModel))

    def test_values_default(self):
        """Check valores de atributo default""" 
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attr_type(self):
        """
        test attribute test
        """
        obj = Place()
        self.assertEqual(type(obj.city_id), str)
        self.assertEqual(type(obj.user_id), str)
        self.assertEqual(type(obj.name), str)
        self.assertEqual(type(obj.description), str)
        self.assertEqual(type(obj.number_rooms), int)
        self.assertEqual(type(obj.number_bathrooms), int)
        self.assertEqual(type(obj.max_guest), int)
        self.assertEqual(type(obj.price_by_night), int)
        self.assertEqual(type(obj.latitude), float)
        self.assertEqual(type(obj.longitude), float)
        self.assertEqual(type(obj.amenity_ids), list)
        self.assertTrue(issubclass(Place, BaseModel))

    def test_instances_str(self):
        """chequeamos distintas instancias de tipo str"""
        obj = Place()
        obj.city_id = "Santa Rosa"
        obj.user_id = "vale12"
        obj.name = "Naruto"
        obj.description = "muy agradable"

        self.assertEqual(type(obj.city_id), str)
        self.assertEqual(type(obj.user_id), str)
        self.assertEqual(type(obj.name), str)
        self.assertEqual(type(obj.description), str)

    def test_instances_num(self):
        """chequeamos distintas instancias de tipo number"""
        obj = Place()
        obj.number_rooms = 2
        obj.number_bathrooms = 1
        obj.max_guest = 1

        self.assertEqual(type(obj.number_rooms), int)
        self.assertEqual(type(obj.number_bathrooms), int)
        self.assertEqual(type(obj.max_guest), int)

    def test_instances_float(self):
        """chequeamos instancias de tipo float"""
        obj = Place()
        obj.latitude = 2.2
        obj.longitude = 4.0

        self.assertEqual(type(obj.latitude), float)
        self.assertEqual(type(obj.longitude), float)

    def test_inst_list(self):
        """instancia de tipo lista"""
        obj = Place()
        obj.amenity_ids = ["Balcon"]

        self.assertEqual(type(obj.amenity_ids), list)

    def test_dif_id(self):
        """test diferentes ids"""
        obj1 = Place()
        obj2 = Place()

        self.assertNotEqual(obj1.id, obj2.id)

    def test_documentation(self):
        """
        chequeamos la documentacion
        """
        self.assertIsNotNone(Place.__doc__)    

if __name__ == '__main__':
    unittest.main()
