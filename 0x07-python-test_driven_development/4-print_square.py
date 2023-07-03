#!/usr/bin/python3
"""this module defines print_square"""


def print_square(size):
    """prints size of square using the # symbol"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size) + "\n") * size, end="")
