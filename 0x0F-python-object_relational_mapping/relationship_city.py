#!/usr/bin/python3
'''
Creation of a new file, relationship_city for the
City class from models_city
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
