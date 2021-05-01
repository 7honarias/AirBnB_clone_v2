#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    name = ""
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')

    def __init__(self, *argv, **kargs):
        """initialization"""
        super().__init__(*argv, **kargs)

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        """return list of cities"""
        @property
        def cities(self):
            """methodo"""
            list_cities = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
