#!/usr/bin/python3
"""
TEST OF CLASS AMENITY
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.engine.file_storage import FileStorage


class test_fileStorage(unittest.TestCase):
    """
    File_Storage test
    """

    def test_documentation(self):
        """
        test documentation
        """
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_is_an_instance(self):
        """
        test instantation
        """
        test = FileStorage()
        self.assertIsInstance(test, FileStorage)


    if __name__ == '__main__':
        unittest.main()