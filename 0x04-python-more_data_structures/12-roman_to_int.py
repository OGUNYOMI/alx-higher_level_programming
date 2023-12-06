#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for char in roman_string[::-1]:
        curr_value = roman_numerals[char]

        if curr_value >= prev_value:
            total += curr_value
        else:
            total -= curr_value

        prev_value = curr_value

    return total
