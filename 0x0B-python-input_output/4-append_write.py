#!/usr/bin/python3
"""Module 4-append_write
A function that appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """Appends text to the filename with Args:
    - filename: name of the file
    - text: the text to append

    Return: the number of char added
    """

    with open(filename, mode="a", encoding="utf8") as a_file:
        return a_file.write(text)
