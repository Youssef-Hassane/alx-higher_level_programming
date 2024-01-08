#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    for row in matrix:
        for columnIndex, column in enumerate(row):
            print("{:d}".format(column), end="")
            if columnIndex < len(row) - 1:
                print(" ", end="")
        print()
