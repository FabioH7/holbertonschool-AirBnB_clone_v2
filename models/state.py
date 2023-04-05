#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="delete")

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            new_ls = []
            for city in models.storage.all("City").values():
                if self.id == city.state_id:
                    new_ls.append(city)
            return new_ls
