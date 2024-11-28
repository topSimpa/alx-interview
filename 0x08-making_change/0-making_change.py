#!/usr/bin/python3
"""
    Module for making_change Solution
"""


def makeChange(coins, total) -> int:
    """makechange function"""

    divd = total
    pre_divd = total
    count = 0
    pre_minus = 0
    to_minus = 0

    if total <= 0:
        return (0)

    while (total > 0):
        for coin in coins:
            if ((total // coin) <= divd) and ((total // coin) != 0):
                to_minus = coin
                divd = total // coin

        if (divd == pre_divd and pre_minus == to_minus):
            return (-1)
        count += divd
        total -= (divd * to_minus)
        pre_minus = to_minus
        pre_divd = total
        divd = total

    return (count)
