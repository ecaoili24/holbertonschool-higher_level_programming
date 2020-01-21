#!/usr/bin/python3
"""Module 7-save_to_json_file
A function that writes an object to a text file by
using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes the rep for my_obj to filename with Args:
    - my_obj: the obj to write
    - filename: the file to write into
    """

    with open(filename, mode="w", encoding="utf8") as a_file:
        return a_file.write(json.dumps(my_obj))
