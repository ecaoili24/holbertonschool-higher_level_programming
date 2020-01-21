#!/usr/bin/python3
"""Module 10-square
Creates a Square class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square
    Private instance with  attribute size.
    Public method area().
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """Initializes a Square with Args:
        size: a size of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a formatted string"""
        return str("[Square] {:d}/{:d}".format(self.__size, self.__size))

    def area(self):
        """Gets the area of a Square instance.
        Replaces the area() method from Rectangle.
        """

        return self.__size ** 2
