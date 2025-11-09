#!/usr/bin/python3

def siyahi(my_list=[], x=0):
    say = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            say += 1
        except IndexError:
            break
    print()
    return say