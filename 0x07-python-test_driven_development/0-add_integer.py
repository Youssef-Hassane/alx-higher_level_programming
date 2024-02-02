#!/usr/bin/python3
"""Module for function that adds 2 integers"""


def add_integer(a, b=98):
    """Add two integers and return the result

    Args:
        a: First number, must be an integer or float.
        b: Second number, must be an integer or float (defaults to 98).

    Raises:
        TypeError: If either of a or b is neither an integer nor a float.

    Returns:
        int: The sum of a and b after casting them to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
