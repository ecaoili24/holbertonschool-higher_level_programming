#!/usr/bin/python3
'''
Script that adds the State object “Louisiana” to the
database hbtn_0e_6_usa
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

    NEW_state = State(name='Louisiana')
    session.add(NEW_state)
    session.commit()

    for state in session.query(State).order_by(State.id).all():
        if state.name == 'Louisiana':
            print(state.id)

    session.close()
