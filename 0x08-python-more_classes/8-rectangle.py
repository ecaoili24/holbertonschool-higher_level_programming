#!/usr/bin/python3
"""Module that defines a Rectangle Class"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height
    """
    Initializes a Rectangle instance

    Arguments:
    width: width of the rectangle
    height: height of the rectangle
    """
    @property
    def width(self):
        return self.__width
    """gets the width of a Rectangle instance"""

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """gets the height of a Rectangle instance"""
    @property
    def height(self):
        return self.__height

    """
    sets the height of Rectangle instance.
    Argument: value of the height and must be
    a positive number
    """

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height
    """
    calculates the area of a Rectangle instance

    Returns:Area of the rectangle, given by heart * width
    """

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
    """
    calculates the perimeter of a Rectangle instance

    Returns: Perimeter of the rectangle, given by 2 *
    (height + width)
    """

    def __str__(self):
        s = ""
        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                for x in range(self.__width):
                    s = str(self.print_symbol)
                s = s + "\n"
        return s[: -1]
    """
    Returns an informal and printable string
    representation of a Rectangle instance. It is
    filled with the "#" character
    """

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height)
    """
    Returns a string representation of a Rectangle instance. It is able
    to recreate a new instance by using eval()
    """

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances += -1
    """deletes the rectangle instance"""

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
    """
    finds the biggest Rectangle based on the area.
    Arguments: rect 1 = Rectangle instance and rect_2 =
    different from rect_1
    """
