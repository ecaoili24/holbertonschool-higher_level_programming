#!/usr/bin/python3
"""Module 4-inherits_from.
Finds an object if it's an instance of a class that is inherited
--diirectly or indirectly from the specified class."""


def inherits_from(obj, a_class):
    return isinstance(obj, a_class) and type(obj) is not a_class

    """Evaluates if an obj is an instance of a class that's
    inherited from a_class.
    Args:
        - obj: object to look at
        - a_class: class to check

    Returns: True or False
    """
