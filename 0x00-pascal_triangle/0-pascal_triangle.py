#!/usr/bin/python3
"""
defines a function that compute pascal triangle
"""


def pascal_triangle(n):
    """Implements pascals triangle use for series expansion.
    calculate the coefficient of the first nth pascal"""
    coefs = []
    if n <= 0:
        return coefs
    j = 0
    while j < n:
        new = []
        i = 0
        while i <= j:
            if i == 0 or i == j:
                new.append(1)
            else:
                new.append(coefs[j - 1][i - 1] + coefs[j - 1][i])
            i += 1
        coefs.append(new)
        j += 1
    return coef
