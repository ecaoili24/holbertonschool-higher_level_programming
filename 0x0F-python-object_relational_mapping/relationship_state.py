#!/usr/bin/python3
'''
Create relationship_state file from models_state file. The class attribute
cities must represent a relationship with the class City.
If the State object is deleted, all linked City objects must be
automatically deleted. Also, the reference from a City object
to his State should be named state
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City, Base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
