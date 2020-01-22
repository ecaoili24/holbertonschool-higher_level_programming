#!/usr/bin/python3
"""Module 2-read_lines.py
A function that reads n lines of a text file (UTF8) and prints it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """Reads and prints nb_lines from filename with Args:
    - filename: the name of the file
    - nb_lines: the number of lines to read
    """

    with open(filename, encoding="utf8") as a_file:
        if nb_lines <= 0:
            print(a_file.read(), end="")
        else:
            for line in range(nb_lines):
                print(a_file.readline(), end="")
