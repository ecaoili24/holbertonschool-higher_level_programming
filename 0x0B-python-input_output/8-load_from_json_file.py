#!/usr/bin/python3
"""Module 8-load_from_json_file
A function that creates an object from a "JSON file."
"""


import json


def load_from_json_file(filename):
    """Creates an obj from filename with Args:
    - filename: the name of the JSON file

    - Return: the object
    """

    with open(filename, encoding="utf8") as a_file:
        return json.load(a_file)
