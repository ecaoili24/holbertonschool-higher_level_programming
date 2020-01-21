#!/usr/bin/python3
"""Module 1-number_of_lines
A funtion that counts the  number of lines in a file.
"""


def number_of_lines(filename=""):
    """Counts lines in filename with Args:
    - filename: name of the file

    Returns:
    - number of lines
    """

    count = 0

    with open(filename, encoding="utf8") as the_file:
        for lin in the_file:
            count += 1
        return count
