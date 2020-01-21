#!/usr/bin/python3
"""Module 5-to_json_string
A function that returns the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """Returns the JSON represenation of an object with Args:
    - my_obj: a string to represent
    Return: JSON rep
    """

    return json.dumps(my_obj)
