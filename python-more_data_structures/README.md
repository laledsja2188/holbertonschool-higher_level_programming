# Python - More Data Structures: Set, Dictionary

This directory contains Python exercises focused on advanced data structures, particularly sets and dictionaries.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What are sets and how to use them
- What are the most common methods of set and how to use them
- When to use sets versus lists
- How to iterate over a set
- What are dictionaries and how to use them
- When to use dictionaries versus lists or sets
- What is a key in a dictionary
- How to iterate over a dictionary
- What is a lambda function
- What are the map, reduce and filter functions

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

## Tasks

### 0. Squared simple
**File:** `0-square_matrix_simple.py`

Write a function that computes the square value of all integers of a matrix.

- Prototype: `def square_matrix_simple(matrix=[]):`
- `matrix` is a 2 dimensional array
- Returns a new matrix:
  - Same size as `matrix`
  - Each value should be the square of the value of the input
- Initial matrix should not be modified
- You are not allowed to import any module
- You are allowed to use regular loops, map, etc.

**Example:**
```python
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
```

**Output:**
```
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## Repository Information

- **GitHub repository:** holbertonschool-higher_level_programming
- **Directory:** python-more_data_structures
- **Author:** Lal Ciftci
- **School:** Holberton School

## Environment

- **Language:** Python 3.8.5
- **OS:** Ubuntu 20.04 LTS  
- **Style guidelines:** pycodestyle (version 2.8.*)
- **Interpreter:** `/usr/bin/python3`

## Data Structures Covered

### Sets
- **Definition:** Unordered collection of unique elements
- **Use cases:** Removing duplicates, membership testing, mathematical operations
- **Methods:** `add()`, `remove()`, `discard()`, `union()`, `intersection()`, `difference()`

### Dictionaries
- **Definition:** Ordered collection of key-value pairs
- **Use cases:** Data mapping, fast lookups, counting, grouping
- **Methods:** `get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`

### Advanced Functions
- **Lambda functions:** Anonymous functions for short operations
- **Map function:** Apply function to all items in iterable
- **Filter function:** Filter items from iterable based on condition
- **Reduce function:** Apply function cumulatively to items

## Best Practices

1. **Choose right data structure:**
   - Use `list` for ordered, mutable sequences
   - Use `tuple` for ordered, immutable sequences  
   - Use `set` for unique elements and set operations
   - Use `dict` for key-value mappings

2. **Performance considerations:**
   - Dictionary lookup: O(1) average case
   - Set membership test: O(1) average case
   - List search: O(n) linear time

3. **Memory efficiency:**
   - Sets and dicts use hash tables (more memory but faster)
   - Lists use arrays (less memory but slower for lookups)