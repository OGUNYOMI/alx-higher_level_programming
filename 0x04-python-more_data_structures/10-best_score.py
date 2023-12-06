#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_value = max(a_dictionary.values())
    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key
