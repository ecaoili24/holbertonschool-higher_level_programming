#!/usr/bin/python3
'''
script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
'''

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.schema import Table

if __name__ == "__main__":

    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)

    Base.metadata.create_all(eng)

    session = Session(eng)

    NEW_city = City(name='San Francisco')
    NEW = State(name='California')
    new.cities.append(NEW_city)
    session.add_all([NEW, NEW_city])

    session.commit()
    session.close()
