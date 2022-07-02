#!/usr/bin/python3
"""
__init__.py can just be an empty file, but it can also execute initialization
code for the package.
Here we are initializing "storage" to create a unique FileStorage
instance for our application.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()  # Create storage as an instance of "FileStorage"
storage.reload()  # Call reload method on "storage" instance