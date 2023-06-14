#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    new_list = []
    for num in my_list:
        new_list.append(num*number)

    return new_list
