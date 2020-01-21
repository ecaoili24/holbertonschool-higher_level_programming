#!/usr/bin/python3
"""Module 12-student.py
Creation of a Student class.
"""


class Student:
    """Class that defines a student with publc attributes:
    first_name, last_name, and age.
    Public method to_json()
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the instance of class, Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets the dictionary representation of a Student
        instance with Args:
        - attrs: list of attributes

        Return: the dictionary rep of the instance
        """

        if attrs is not None:
            dict1 = dict()
            for x in attrs:
                if x in self.__dict__:
                    dict1[x] = self.__dict__[x]
            return dict1
        return self.__dict__
