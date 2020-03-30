#!/usr/bin/python3
'''
Script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connect = MySQLdb.connect(host="localhost",
                              port=3306,
                              user=argv[1],
                              passwd=argv[2],
                              db=argv[3])
    current = connect.cursor()
    current.execute("""SELECT cities.name FROM cities, states WHERE
    cities.state_id = states.id AND states.name = %s""", (argv[4],))

    query_rows = current.fetchall()
    for row in query_rows:
        print(', '.join(city[0] for city in rows))
    current.close()
    connect.close()
