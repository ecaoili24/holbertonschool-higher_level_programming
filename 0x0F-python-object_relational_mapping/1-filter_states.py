#!/usr/bin/python3
'''
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
'''

import MySQLdb
import sys

if __name__ == "__main__":

    connect = MySQLdb.connect(host="localhost",
                              port=3306,
                              user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3],
                              charset="utf8")
    current = connect.cursor()
    current.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' \
 ORDER BY id ASC""")
    query_rows = current.fetchall()
    for row in query_rows:
        print(row)
    current.close()
    connect.close()
