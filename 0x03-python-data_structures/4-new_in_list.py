#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_count = len(my_list)
    new_list = my_list.copy()
    if idx < 0:
        return my_list
    if idx > list_count:
        return my_list
    else:
        new_list[idx] = element
        return my_list

