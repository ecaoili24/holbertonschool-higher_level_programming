#!/usr/bin/python3
"""Module 3-is_kind_of_class.
Finds the object if it's an instance of, or if the object is an
instance of a class that it's inherited from that specified class.
"""


def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)

    """Finds if obj is an instance of a_class or a class
    inherited from a_class.
    Args:
        - obj: object to look at
        - a_class: class to check

    Returns: True or False
    """
