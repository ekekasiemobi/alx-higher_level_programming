#!/usr/bin/python3
"""Tests case for rectangle.py"""

from models.rectangle import Rectangle
from models.base import Base
import unittest


def setUp(self):
    Base._Base__nb_objects = 0

class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        r = Rectangle(8, 10, 4, 6, 2)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 6)
        self.assertIsNotNone(r.2)

    def test_rectangle_defalut_atrr(self):
        r = Rectangle(8, 10)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)


class TestRectangle_width(unittest.TestCase):

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(None, 10)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("hello", 10)

     def test_invalid_width(self):
        with self.assertRaisesRegex(ValueError, "width must be greater than zero"):
            r = Rectangle(0, 10)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("8.27", 10)

class TestRectangle_height(unittest.TestCase):

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(8, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(8, "hello")

     def test_invalid_height(self):
        with self.assertRaisesRegex(ValueError, "width must be greater than zero"):
            r = Rectangle(8, 0)

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(8, 10.27)

class TestRectangle_x(unittest.TestCase):

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(8, 10, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(8, 10, "hello")

     def test_invalid_x(self):
        with self.assertRaisesRegex(ValueError, "width must be greater than zero"):
            r = Rectangle(8, 10, 0)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(8, 10, 4.27)

class TestRectangle_y(unittest.TestCase):

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(8, 10, 4, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(8, 10, 4, "hello")

     def test_invalid_y(self):
        with self.assertRaisesRegex(ValueError, "width must be greater than zero"):
            r = Rectangle(8, 10, 4, 0)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(8, 10, 4, 6.27)
