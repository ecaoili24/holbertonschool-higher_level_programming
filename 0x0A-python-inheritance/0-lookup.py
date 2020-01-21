#!/usr/bin/python3
"""Module 0-lookup.
Finds a list of available attributes and methods of an object.
"""


def lookup(obj):
    return dir(obj)


"""Returns a list of attributes and methods.
    Args:
        - obj: object to look into
    """
