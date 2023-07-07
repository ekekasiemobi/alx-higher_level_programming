#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for mat_integer"""

    def test_module_docstring(self):
        """Tests for module docsting"""
        module = __import__('6-max_integer').__doc__
        self.assertTrue(len(module) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        function = max_integer.__doc__
        self.assertTrue(len(function) > 1)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_one_negative(self):
        """Tests list with one negative number"""
        my_list = [20, 80, 30, -40, 10, 50]
        self.assertEqual(max_integer(my_list), 80)

    def test_empty_list(self):
        """Tests for empty list []"""
        my_list = []
        self.assertIsNone(max_integer(my_list))

    def test_max_beginning(self):
        """Test positive value with max at the beginning"""
        my_list = [80, 60, 10, 40, 30, 50]
        self.assertEqual(max_integer(my_list), 80)

     def test_max_end(self):
        """Tests positive with max at the end"""
        my_list = [50, 30, 10, 40, 60, 80]
        self.assertEqual(max_integer(my_list), 80)

    def test_max_middle(self):
        """Tests positive with max in the middle"""
        my_list = [60, 10, 40, 80, 30, 50]
        self.assertEqual(max_integer(my_list), 80)

    def test_all_negative(self):
        """Tests list with all negative values"""
        my_list = [-60, -30, -40, -10, -80]
        self.assertEqual(max_integer(my_list), -10)

if __name__ == "__main__":
    unittest.main()
