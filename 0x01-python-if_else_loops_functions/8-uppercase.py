#!/usr/bin/python3
def uppercase(str):
    for c in str:
        x = ord(c)
        if x >= 97 and x <= 123:
         c = chr(x - 32)
        print(f"{c}", end='')
    print('')

uppercase("best")
uppercase("Best School 98 Battery street")

