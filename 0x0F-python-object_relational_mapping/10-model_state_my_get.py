#!/usr/bin/python3
'''
Script that prints the State object with the name passed as argument
 from the database hbtn_0e_6_usa
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

    flag = 0
    for state in session.query(State).order_by(State.id).all():
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            flag = 1
    if flag == 0:
        print("Not found")

    session.close()
