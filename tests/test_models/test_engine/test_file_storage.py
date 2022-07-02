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
    """Test FileStorage Class"""
    def test_docs(self):
        """chequeamos documentacion"""
        self.assertIsNotNone(FileStorage.new.__doc__)        
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)


    def test_classes(self):
        """check classes"""
        self.assertIsInstance(models.engine.file_storage.FileStorage(),
                              models.engine.file_storage.FileStorage)

    def test_all(self):
        """check all"""
        self.assertIsNotNone(models.engine.file_storage.FileStorage().all)

    def test_new(self):
        """check if new method is working"""

        self.assertIsNotNone(models.engine.file_storage.FileStorage().new)

    def test_save(self):
        """check if save method is working"""

    if __name__ == '__main__':
        unittest.main()