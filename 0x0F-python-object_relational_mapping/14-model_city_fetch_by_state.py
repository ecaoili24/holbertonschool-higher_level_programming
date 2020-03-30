#!/usr/bin/python3
'''
Script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa
'''

import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    eng = create_engine('mysql+mysqldb://' + '{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)

    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)

    session = Session()
    for states, cities in session.query(
            State, City).filter(
            State.id == City.state_id).order_by(City.id).all():
        print('{}: ({}) {}'.format(states.name, cities.id, cities.name))

    session.close()
