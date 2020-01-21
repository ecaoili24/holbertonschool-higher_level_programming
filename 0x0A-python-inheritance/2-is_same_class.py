#!/usr/bin/python3
"""Module 2-is_same_class.
Finds an object if it's exactly an instance of a class.
"""


def is_same_class(obj, a_class):
    return type(obj) == a_class

    """Function to determine if obj is an instance of a_class.
    Args:
        - obj: object to look at
        - a_class: class to verify the instance of

    Return: if obj is an instance of a_class and False if
    otherwise
    """
