#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed = 0

    try:
        while printed < x:
            if isinstance(my_list[count], int):
                print("{:d}".format(my_list[count]), end="\n" if printed == x - 1 else " ")
                printed += 1
            count += 1
        except IndexError:
        pass

    return printed
