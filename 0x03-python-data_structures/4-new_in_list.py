#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_count = len(my_list)
    if idx < 0 or idx >= list_count:
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
    return new_list
