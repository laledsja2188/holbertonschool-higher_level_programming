#!/usr/bin/python3
"""
This module contains a function for text indentation.
It adds 2 new lines after each '.', '?' and ':' character.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): The text to print with indentation

    Raises:
        TypeError: If text is not a string

    Prints:
        Text with 2 new lines after '.', '?' and ':'
        No spaces at the beginning or end of each line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    new_line = True

    while i < len(text):
        char = text[i]
        if char in ".?:":
            print(char)
            print()
            new_line = True
            i += 1
        elif char == " " and new_line:
            i += 1
        else:
            print(char, end="")
            new_line = False
            i += 1
