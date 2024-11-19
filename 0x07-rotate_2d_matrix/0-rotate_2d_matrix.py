#!/usr/bin/python3
""" Module to implement Rotating a 2D matrix
    by 90 degree
"""


def rotate_2d_matrix(matrix):
    """rotate matrix by 90 degree"""
    n = len(matrix)
    for row in range(n):
        for col in range(n):
            if row < col and row < n - 1:
                save = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = save
            if col >= n // 2:
                save = matrix[row][col]
                matrix[row][col] = matrix[row][n - col - 1]
                matrix[row][n - col - 1] = save
