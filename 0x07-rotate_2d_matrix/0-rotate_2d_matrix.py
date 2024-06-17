#!/usr/bin/python3
"""
    Rotate 2D Matrix solution Module
"""


def rotate_2d_matrix(matrix):
    """rotate a matrix 90 degrees clockwise"""
    n = len(matrix)
    for row in range(n):
        if row < (n // 2):
            for col in range((row + 1), n):
                a = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = a
        matrix[row] = matrix[row][::-1]
