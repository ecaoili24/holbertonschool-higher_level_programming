#!/usr/bin/python3
"""
Module text_indentation
Adds two new lines after a set of characters
"""


def text_indentation(text):
    """Prints text and adds two newlines
    after each of these characters {'.', '?', ':'}.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    chars = ['.', '?', ':']
    string = ""
    line_pos = 0

    for delim in text:
        if not (line_pos == 0 and delim == " "):
            string += delim
            line_pos += 1
        if delim in chars:
            string += '\n\n'
            line_pos = 0
    print(string, end="")
