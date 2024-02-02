#!/usr/bin/python3
""" Divide all elements of a matrix by a given divisor """


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): Matrix of integers or floats.
        div (int or float): Divisor.

    Returns:
        list of lists: New matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If the input matrix is not a list
        of lists of integers/floats,
                   or if each row of the matrix does not have the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
        TypeError: If any element of the matrix is not an integer or float.
    """
    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix or not isinstance(matrix, list):
        raise TypeError(
            errorMessage
        )
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(
                errorMessage
            )
        if len(row) != len(matrix[0]):
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    errorMessage
                )
    result_matrix = [[round(element / div, 2)
                      for element in row] for row in matrix]

    return result_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
