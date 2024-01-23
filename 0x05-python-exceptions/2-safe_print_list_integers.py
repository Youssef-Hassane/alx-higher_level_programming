#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x indexs of a list that are integers.

    Args:
        my_list (list): The list to print indexs from.
        x (int): The number of indexs to access in my_list.

    Returns:
        int: The number of integers actually printed.
    """

    count = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            count += 1
        except (TypeError, ValueError):
            pass
    print()
    return count
