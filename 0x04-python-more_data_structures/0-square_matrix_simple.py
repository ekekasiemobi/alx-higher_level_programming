#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for items in matrix:
        new_items = []
        for item in items:
            new_items.append(item ** 2)
        new_matrix.append(new_items)

    return new_matrix
