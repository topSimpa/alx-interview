#!/usr/bin/python3
"""Utf8-Validation  Module
"""


def bytes_counter(num):
    """
    count the number of 1 which interprete to num_bytes of first member of data
    """
    shift_val = num >> 3
    if shift_val >= 0 and shift_val <= 15:
        return 0
    elif shift_val >= 16 and shift_val <= 23:
        return 1
    elif shift_val >= 24 and shift_val <= 27:
        return 2
    elif shift_val >= 28 and shift_val <= 29:
        return 3
    elif shift_val == 30:
        return 4
    return None


def valid_sequence(chars):
    """to check if a byte start with 10
    """
    for char in chars:
        if bytes_counter(char) != 1:
            return False
    return True


def validUTF8(data):
    """Utf8-Validation
       -Validate if coding is in utf8-format
    """
    cur_position = 0
    while cur_position < len(data):
        n_bytes = bytes_counter(data[cur_position])
        if n_bytes == 0:
            cur_position += 1
            continue
        elif n_bytes == 1:
            return False
        elif n_bytes is None:
            return False
        if len(data[cur_position: cur_position + n_bytes]) < n_bytes:
            return False
        if not valid_sequence(data[cur_position + 1: cur_position + n_bytes]):
            return False
        cur_position = cur_position + n_bytes

    return True
