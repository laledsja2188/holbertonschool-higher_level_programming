# Python - Import & Modules

This project contains exercises and tasks related to importing functions and modules in Python.

## Description

Learning objectives:
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the pycodestyle (version 2.8.\*)
- All files must be executable
- The length of files will be tested using `wc`

## Tasks

### 0. Import a simple function from a simple file
**File:** `0-add.py`
- Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`

### 1. My first toolbox!
**File:** `1-calculation.py`
- Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.

### 2. How to make a script dynamic!
**File:** `2-args.py`
- Write a program that prints the number of and the list of its arguments.

### 3. Infinite addition
**File:** `3-infinite_add.py`
- Write a program that prints the result of the addition of all arguments

### 4. Who are you?
**File:** `4-hidden_discovery.py`
- Write a program that prints all the names defined by the compiled module `hidden_4.pyc`

### 5. Everything can be imported
**File:** `5-variable_load.py`
- Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.

## Files

| Filename | Description |
|----------|-------------|
| `0-add.py` | Import and use add function |
| `add_0.py` | Contains add function |
| `1-calculation.py` | Import and use calculator functions |
| `calculator_1.py` | Contains calculator functions |
| `2-args.py` | Handle command line arguments |
| `3-infinite_add.py` | Add infinite number of arguments |
| `4-hidden_discovery.py` | Discover names in compiled module |
| `hidden_4.pyc` | Compiled module |
| `5-variable_load.py` | Import and print variable |
| `variable_load_5.py` | Contains variable |
| `0-import_add.py` | Test import without execution |

## Usage Examples

```bash
# Task 0 - Import a simple function
./0-add.py
# Output: 1 + 2 = 3

# Task 1 - Calculator operations  
./1-calculation.py
# Output: 10 + 5 = 15
#         10 - 5 = 5
#         10 * 5 = 50
#         10 / 5 = 2

# Task 2 - Command line arguments
./2-args.py
# Output: 0 arguments.

./2-args.py Hello
# Output: 1 argument:
#         1: Hello

# Task 3 - Infinite addition
./3-infinite_add.py 79 10
# Output: 89

# Task 4 - Hidden discovery
./4-hidden_discovery.py
# Output: my_secret_santa
#         print_hidden
#         print_school

# Task 5 - Variable import
./5-variable_load.py
# Output: 98
```

## Author

**Lal Ciftci**
- GitHub: [@laledsja2188](https://github.com/laledsja2188)

## Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-import_modules`