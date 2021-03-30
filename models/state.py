#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """update"""
    
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship('City', cascade='all, delete-orphan',
                          backref='state')
