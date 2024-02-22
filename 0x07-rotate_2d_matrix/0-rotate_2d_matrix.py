#!/usr/bin/python3
""" Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """ function to rotate a matrix 90 degrees clockwise
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
