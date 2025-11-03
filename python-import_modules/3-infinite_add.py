#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    arguments = sys.argv[1:]
    
    sum = 0
    
    for argument in arguments:
        number = int(argument)
        sum = sum + number
    
    print(sum)