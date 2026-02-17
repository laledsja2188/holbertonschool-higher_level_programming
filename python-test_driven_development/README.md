# Python - Test-driven development

This directory contains projects focused on Test-Driven Development (TDD) in Python.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What's an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

## Tasks

### 0. Integers addition
Write a function that adds 2 integers.

- **Prototype**: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception
- `a` and `b` must be first casted to integers if they are float
- Returns an integer: the addition of a and b
- You are not allowed to import any module

**Files**: `0-add_integer.py`, `tests/0-add_integer.txt`

## Testing

Run the tests using:
```bash
python3 -m doctest -v ./tests/0-add_integer.txt
```

## Author

**Student** - Holberton School