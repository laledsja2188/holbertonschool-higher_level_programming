# Simple Shell Project

This is my attempt at creating a simple shell for Holberton School.

## What it does

Basically, it's supposed to work like a basic version of bash or sh. You type commands and it tries to run them.

## How to compile

```
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 *.c -o hsh
```

I think this should work but I'm not 100% sure about all the flags.

## How to use it

Run it like this:
```
./hsh
```

Then you can try commands like:
- ls
- pwd
- /bin/echo hello
- exit (to quit)

## What works (hopefully)

- Running basic commands
- The exit command
- Maybe the env command
- Error messages when you type wrong stuff

## Files

- shell.h - has all the function prototypes and stuff
- main.c - main function where everything starts
- Other .c files - different functions split up

## Notes

Still working on some bugs. The PATH handling might not be perfect yet.

## Authors

Check the AUTHORS file.
