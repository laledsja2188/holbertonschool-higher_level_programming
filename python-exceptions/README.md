# Python - Exceptions

This directory contains Python scripts that demonstrate exception handling.

## Files

- `0-safe_print_list.py`: A function that prints x elements of a list safely using exception handling.

## Description

The `siyahi` function safely prints the first x elements of a list, handling IndexError exceptions when the list is shorter than the requested number of elements.

### Usage

```python
def siyahi(my_list=[], x=0):
    """
    Safely prints x elements of a list
    
    Args:
        my_list: List to print from
        x: Number of elements to print
        
    Returns:
        Number of elements actually printed
    """
```

## Learning Objectives

- How to handle exceptions in Python
- Understanding try/except blocks
- Working with IndexError exceptions
- Safe list element access