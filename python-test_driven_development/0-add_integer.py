#!/usr/bin/python3
"""
This module contains a function for adding two integers.
It handles type checking and casting for integers and floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers after type checking and casting.

    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98

    Returns:
        int: The sum of a and b as integers

    Raises:
        TypeError: If a or b is not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b
