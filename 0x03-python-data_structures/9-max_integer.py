#!/usr/bin/python3

def max_integer(my_list=[]):
    list_count = len(my_list)
    max_value = my_list[0]
    if list_count == 0:
        return None
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value
