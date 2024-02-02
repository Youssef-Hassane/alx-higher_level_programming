#!/usr/bin/python3
""" Defines a function that prints a square with the character # """


def print_square(size):
    """
    Print a square of a given size using the character '#'.

    Args:
        size (int): Size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and is less than 0.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # Check if size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")
    # Check if size is a float and is less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    # Print the square
    for _ in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
