#!/usr/bin/python3
"""Module 0-read_file
A function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Reads from filename and prints its
    contents to stdout. With Args:
    - filename: name of the file
    """

    with open(filename, encoding="utf-8") as the_file:
        print(the_file.read(), end="")
