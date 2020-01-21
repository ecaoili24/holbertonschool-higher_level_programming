#!/usr/bin/python3
"""Unittest for max_integer([..]) module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([2, 4, 6]), 6)
        self.assertEqual(max_integer([4, 2, 1]), 4)
        self.assertEqual(max_integer([1, 10, 8]), 10)
        self.assertEqual(max_integer([-1, 2, 4]), 4)
        self.assertEqual(max_integer([-1, -5, -6]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))
