#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import models
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
