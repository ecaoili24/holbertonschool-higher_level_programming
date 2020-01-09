#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print("")
