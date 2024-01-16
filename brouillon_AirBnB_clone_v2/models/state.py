#!/usr/bin/python3
"""
State module
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """
    State class that inherit from BaseModel
"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="delete")
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ Getter method that gets a
            list of cities with the same stateid
            """
            allCities = models.storage.all(City)
            citiesList = [city for city in allCities.values()
                            if city.state_id == self.id]
            return citiesList