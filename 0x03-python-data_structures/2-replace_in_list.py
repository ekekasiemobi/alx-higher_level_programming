#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    list_count = len(my_list)
    if idx < 0:
        return my_list
    if idx > list_count:
        return my_list
    else:
        my_list[idx] = element
        return my_list
