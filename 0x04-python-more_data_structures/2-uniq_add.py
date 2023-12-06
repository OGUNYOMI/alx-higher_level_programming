#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()
    sum_unique = 0

    for num in my_list:
        if num not in unique_integers:
            sum_unique += num
            unique_integers.add(num)

    return sum_unique
