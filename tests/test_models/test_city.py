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
    def tests_instances_attr(self):
        """chequeamos attr(type, value), subclass"""
        self.assertTrue('state_id' in City.__dict__)
        self.assertTrue('name' in City.__dict__)


if __name__ == '__main__':
  unittest.main()