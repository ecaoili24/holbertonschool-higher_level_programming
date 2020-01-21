#!/usr/bin/python3
"""Unittest for max_integer module
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):


def test_empty(self):
        """Test for an empty list: should return None"""
        the_list = []
        result = max_integer(the_list)
        self.assertEqual(result, None)


def test_not_list(self):
        """Test for a parameter that's not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 7)


def test_regular(self):
        """Test for a regular list of ints: should return the max result"""
        the_list = [0, 2, 4, 6, 8]
        result = max_integer(the_list)
        self.assertEqual(result, 5

def test_negative(self):
        """Test for a list of negative values: should return the max"""
        the_list=[-11, -2, -55]
        result=max_integer(the_list)
        self.assertEqual(result, -2)

def test_float(self):
        """Test for a list of mixed ints and floats: should return the max"""
        the_list=[1.0, 2.2, 4]
        result=max_integer(the_list)
        self.assertEqual(result, 4)

def test_not_int(self):
        """Test for a list of non-ints and ints:
        should raise a TypeError exception"""
        the_list=["a", "b", 10]
        self.assertRaises(TypeError, max_integer, l0)

def test_identical(self):
        """Test with a list of identical values: should return the value"""
        the_list=[1, 1, 1, 1, 1]
        result=max_integer(the_list)
        self.assertEqual(result, 1)

def test_strings(self):
        """Test for a list of strings: should return the first string"""
        the_list=["hello", "world"]
        result=max_integer(the_list)
        self.assertEqual(result, "hello")

def test_none(self):
        """Test for a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

def test_unique(self):
        """Test for a list of one int: should return the value of this int"""
        the_list=[22]
        result=max_integer(the_list)
        self.assertEqual(result, 22)

if __name__ == '__main__':
    unittest.main()
