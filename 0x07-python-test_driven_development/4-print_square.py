#!/usr/bin/python3
"""
This module contains the text_indentation function
"""


def print_square(size):
    """
    Result prints a square where size is the len and width
    of the square
    """
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is 0:
        print("", end="")
    for i in range(size):
        for k in range(size):
            print("#", end="")
        print()
