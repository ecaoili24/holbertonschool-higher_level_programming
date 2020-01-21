#!/usr/bin/python3
"""Module 11-student.py
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

    def to_json(self):
        """Gets the dictionary representation of a Student
        instance

        Return: the dictionary rep of the instance
        """

        return self.__dict__
