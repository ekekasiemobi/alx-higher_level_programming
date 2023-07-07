#!/usr/bin/python3
""" prints a text with new line"""

def text_indentation(text):
    """ function that prints a new line after a symbol"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    symbol = ".?:"
    space = 0
    for i in text:
        if i == " " and space == 0:
            continue
        print(i, end="")
        space = 1
        if i in symbol:
            print("\n")
            space = 0
