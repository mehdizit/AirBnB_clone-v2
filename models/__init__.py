#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models import storage
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
