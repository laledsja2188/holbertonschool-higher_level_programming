#!/usr/bin/python3
"""
This module contains a function for printing squares.
It handles integer validation and size constraints.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size length of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0

    Prints:
        A square of '#' characters with given size
    """
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
