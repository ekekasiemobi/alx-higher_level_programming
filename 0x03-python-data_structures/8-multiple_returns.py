#!/usr/bin/python3

def multiple_returns(sentence):
    first = " "
    length = len(sentence)
    for letters in sentence:
        if length == 0:
            first += None
            return (length, first)
        else:
            first += sentence[0]
            return (length, first)
