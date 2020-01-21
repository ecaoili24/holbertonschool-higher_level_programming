#!/usr/bin/python3
"""Module 1-my_list.
Creates a class MyList that inherits from the list class.
"""

"""Class MyList inherits from list."""


class MyList(list):
    def print_sorted(self):
        newList = sorted(self[:])
        print("{}".format(newList))
