#!/usr/bin/python3
"""module containing an adder function to be tested"""


def add_integer(a, b=98):
    """adds integers
        Arguments:
        @a: first integer
        @b: second integer, defaults to 98 if not provided
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
