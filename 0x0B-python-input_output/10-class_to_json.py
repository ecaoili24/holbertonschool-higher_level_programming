#!/usr/bin/python3
"""Module 10-class_to_json.py
A function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
 for JSON serialization of an object
"""


def class_to_json(obj):
    """Creates a dictionary decription of object with Args:
    - obj: the object to serialize
    - Return: the dictionary description of object
    """

    return obj.__dict__
