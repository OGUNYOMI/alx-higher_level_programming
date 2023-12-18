#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0

    try:
        for item in my_list:
            if printed < x:
                if isinstance(item, int):
                    print("{:d}".format(item), end=" ")
                    printed += 1
            else:
                break
    except TypeError:
        pass

    print()
    return printed
