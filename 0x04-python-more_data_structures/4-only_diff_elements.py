#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    result = []
    for letter in set_1:
        if letter not in set_2:
            result.append(letter)

    for letter in set_2:
        if letter not in set_1:
            result.append(letter)

    return result
