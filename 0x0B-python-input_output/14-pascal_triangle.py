#!/usr/bin/python3
"""Module 14-pascal_triangle.py
A function that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Returns the Pascal Triangle of n with Args:
    - n: the size of the triangle in rows

    Return: the list of list of int
    """
    pascal_triangle = []
    for x in range(n):
        row = []
        for y in range(x + 1):
            row.append(factorial(x) // (factorial(y) * factorial(x - y)))
        pascal_triangle.append(row)
    return pascal_triangle

    if n <= 0:
        return []
    """Returns an empty list if n <= 0"""


def factorial(num):
    factorial = 1
    for x in range(1, num + 1):
        factorial = factorial * x
    return factorial
