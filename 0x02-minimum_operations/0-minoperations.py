#!/usr/bin/python3
"""solution to minimum Operation interview question"""


def copy(k, op):
    """carry out the copy operations"""
    return (k, op + 1)


def paste(k, c, op):
    """carry out the paste operations"""
    return (k + c, op + 1)


def minOperations(n):
    """calculate the minioperation needed for nH"""
    if n <= 1 and type(n) != 'int':
        return (0)
    op, k = 2, 2
    c = 1
    while k < n:
        if (n % k == 0):
            c, op = copy(k, op)
            k, op = paste(k, c, op)
        else:
            k, op = paste(k, c, op)
    return (op)
