#!/usr/bin/python3
"""Tests case for rectangle.py"""

from models.rectangle import Rectangle
from models.base import Base
import unittest


def setUp(self):
    Base._Base__nb_objects = 0

class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        r = Rectangle(5, 10, 6, 7, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 7)
        self.assertIsNotNone(r.1)

    def test_rectangle_defalut_atrr(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)


class TestRectangle_width(unittest.TestCase):
    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("hello", 2)

     def test_invalid_width(self):
        with self.assertRaisesRegex(ValueError, "width can not be zero"):
            r = Rectangle(0, 10)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("five", 10)
