#!/usr/bin/python3
"""
   Module for Prime Game problem
"""


def firstPrime(array):
    """find the first prime number in array"""

    for num in array:
        pos_factor = list(range(2, (num // 2) + 1))
        if (pos_factor == []) and (num != 1):
            return (num)
        for fac in pos_factor:
            if num % fac == 0:
                break
            if fac == pos_factor[-1]:
                return (num)
    return (None)


"""print(firstPrime([4, 5, 6, 8, 9]))
print(firstPrime([4, 6, 8]))
print(firstPrime([4, 6, 8, 2]))"""


def isWinner(x, nums):
    """find who is the winner in the prime game"""
    count_dict = {'M': 0, 'B': 0}
    for rnd in range(3):
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
