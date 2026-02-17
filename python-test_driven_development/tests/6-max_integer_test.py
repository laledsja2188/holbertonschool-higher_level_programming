#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for max_integer function"""

    def test_max_at_end(self):
        """Test with max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with max at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with max in the middle"""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_negative(self):
        """Test with one negative number"""
        self.assertEqual(max_integer([1, -2, 4, 3]), 4)

    def test_all_negative(self):
        """Test with all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_one_element(self):
        """Test with one element in list"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)

    def test_ints_and_floats(self):
        """Test with a mixed list of ints and floats"""
        self.assertEqual(max_integer([1, 2.5, 3.1, 4]), 4)

    def test_string(self):
        """Test with a string (should treat as list of chars)"""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_list_of_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")


if __name__ == '__main__':
    unittest.main()
