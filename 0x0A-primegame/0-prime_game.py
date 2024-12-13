#!/usr/bin/python3
"""
   Module for Prime Game problem
"""


def is_prime(num):
    """check if a number is prime"""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def firstPrime(array):
    """find the first prime number in array"""
    for num in array:
        if is_prime(num):
            return (num)
    return (None)


def isWinner(x, nums):
    """find who is the winner in the prime game"""
    count_dict = {'M': 0, 'B': 0}
    for rnd in range(x):
        num = nums[rnd]
        array = list(range(1, num + 1))
        key = 'M'
        while len(array) > 0:
            pick_num = firstPrime(array)
            if pick_num is None:
                count_dict[key] += 1
                break
            del_num = set(list(range(pick_num, num + 1, pick_num)))
            array = list(set(array).difference(del_num))
            if key == 'M':
                key = 'B'
            else:
                key = 'M'

    if count_dict['M'] > count_dict['B']:
        return ('Ben')
    elif count_dict['B'] > count_dict['M']:
        return ('Maria')
    return (None)
