#!/usr/bin/python3
"""
TEST OF CLASS AMENITY
"""
from datetime import datetime
import unittest
from time import sleep
import json
import models
from models.engine.file_storage import FileStorage


class test_fileStorage(unittest.TestCase):

    def test_classes(self):
        self.assertIsInstance(models.engine.file_storage.FileStorage(),
                              models.engine.file_storage.FileStorage)

    def test_all(self):
        self.assertIsNotNone(models.engine.file_storage.FileStorage().all)

    def test_new(self):
        self.assertIsNotNone(models.engine.file_storage.FileStorage().new)

    def test_save(self):
        self.assertIsNotNone(models.engine.file_storage.FileStorage().save)

    def test_reload(self):
        self.assertIsNotNone(models.engine.file_storage.FileStorage().reload)

    def test_all_method(self):
        self.assertIsNotNone(models.engine.file_storage.FileStorage().all())

    def test_models_all(self):
        self.assertIsNotNone(models.storage.all())    
        
    def test_doc(self):
        self.assertIsNotNone(models.engine.file_storage.FileStorage.__doc__)
        self.assertIsNotNone(models.engine.file_storage.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             all.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             __init__.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             new.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             save.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             reload.__doc__)

    if __name__ == '__main__':
        unittest.main()