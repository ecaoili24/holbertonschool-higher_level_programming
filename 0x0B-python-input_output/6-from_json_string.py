#!/usr/bin/python3
"""Module 6-from_json_string
A function that returns an object (Python data structure)
represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """Returns the obj rep by my_str with Args:
    - my_str: JSON string rep

    Return: corresponding obj
    """

    return json.loads(my_str)
