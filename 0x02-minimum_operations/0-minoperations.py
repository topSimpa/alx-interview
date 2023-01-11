#!/usr/bin/python3
"""solution to minimum Operation interview question"""
from typing import Tuple


def copy(k: int, op: int) -> Tuple[int]:
    """carry out the copy operations"""
    return (k, op + 1)

def paste(k: int, c: int, op: int) -> Tuple[int]:
    """carry out the paste operations"""
    return (k + c, op + 1)

def minOperation(n: int) -> int:
    """calculate the minioperation needed for nH"""
    if n <= 1:
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
