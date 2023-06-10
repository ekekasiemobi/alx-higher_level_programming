#!/usr/bin/python3

def element_at(my_list, idx):
    list_count = len(my_list)
    if idx < 0:
        return None
    if idx > list_count:
        return None
    else:
        return idx

