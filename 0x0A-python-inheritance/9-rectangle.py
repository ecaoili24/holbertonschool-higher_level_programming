#!/usr/bin/python3
"""Module 9-rectangle.
Creates a Rectangle class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with Private instance attributes:
    - width and height
    Public method area()
    Inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Initializes an instance with Args:
        - width: size of the rectangle
        - height: size of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a formatted string"""

        return str("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def area(self):
        """Gets the area of the Rectangle instance.
        Replaces the area() method from BaseGeometry.
        """

        return self.__height * self.__width
