#!/usr/bin/python3
# Write a function that computes the square value of all integers of a matrix.
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = [[0] * len(row) for row in matrix]

    # Iterate through each element of the matrix and compute the square
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
