#!/usr/bin/python3

"""
This module contains the add_integer function
"""


def add_integer(a, b=98):
    """
    Return sum of a and b. Prints an error
    message if a and b are not int or floats
    """
    if type(a) == float:
        a = int(a)
    elif type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) == float:
        b = int(b)
    elif type(b) != int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
