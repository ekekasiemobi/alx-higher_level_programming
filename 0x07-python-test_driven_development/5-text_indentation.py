#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    symbol = [".", "?", ":"]
    result = ""
    i = 0

    word_length = len(text)
    while i < word_length:
        result += text[i]

        if text[i] in symbol:
            result += "\n\n"

        i += 1
    print (result)
