#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    arguments = sys.argv[1:]
    number_of_args = len(arguments)
    
    if number_of_args == 0:
        print("0 arguments.")
    elif number_of_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number_of_args))
    
    i = 1
    for arg in arguments:
        print("{}: {}".format(i, arg))
        i = i + 1