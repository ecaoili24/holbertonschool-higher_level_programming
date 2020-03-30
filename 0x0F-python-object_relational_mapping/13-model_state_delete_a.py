#!/usr/bin/python3
'''
Script that deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa
'''

import MySQLdb
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)

    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)

    session = Session()

    for state in session.query(State).order_by(State.id).all():
        if 'a' in state.name:
            session.delete(state)
    session.commit()

    for state in session.query(State).order_by(State.id).all():
        print('{}: {}'.format(state.id, state.name))
    session.close()
