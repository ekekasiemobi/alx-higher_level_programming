#!/usr/bin/python3
"""Test cases for square.pyS"""
import io
from models.square import Square
from models.base import Base
import unittest


class TestSquare(unittest.TestCase):

     def test_init(self):
        Base._Base__nb_objects = 0
        s = Square(10)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s2.width, 10)
        self.assertEqual(s2.height, 10)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_init_with_given_attr(self)
        s = Square(10, 4, 6, 2)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 6)

    def test_size_property(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_string_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(10.27)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, None)

    def test_string_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, "hello")

     def test_invalid_x(self):
        with self.assertRaisesRegex(ValueError, "x must be greater than zero"):
            r = Rectangle(10, 0)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 4.27)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 4, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 4, "hello")

     def test_invalid_y(self):
        with self.assertRaisesRegex(ValueError, "y must be greater than zero"):
            r = Rectangle(10, 4, 0)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 4, 6.27)
