#!/usr/bin/python3
"""Module 3-write_file
Function that writes a string in a text file
"""


def write_file(filename="", text=""):
    """Writes text in filename with Args:
    - filenmae: name of the file
    - text: the string to write in the file

    Returns: the number of characters written
    """

    with open(filename, mode="w", encoding="utf8") as a_file:
        return a_file.write(text)
