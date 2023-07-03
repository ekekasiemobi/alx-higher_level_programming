#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    my_list = [".", "?", ":"]
    result = ""
    i = 0

    while i < len(text):
        result += text[i]

        if text[i] in my_list
            result += "\n\n"

        i += 1
