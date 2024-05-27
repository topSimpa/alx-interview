#!/usr/bin/python3
"""
Main file for utf8_validation
"""


def xtract(num):
    # print(f'integer {num}')
    byte_a = bin(num)[2:]
    # print(f'Extracting from {byte_a}')
    if (len(byte_a) < 8):
        byte_a = ((8 - len(byte_a)) * '0') + byte_a
        # print(f'changed to {byte_a}')
    bits = ''
    for i in byte_a:
        if i == '0':
            bits += i
            break
        bits += i
    # print(bits)
    return (bits)


def is_byte(num):
    return (num < 128)


def many_bytes(num):
    # print(num)
    a_byte = bin(num)[2:]
    # print(a_byte)
    if (len(a_byte) < 8):
        a_byte = ((8 - len(a_byte)) * '0') + a_byte
        # print(a_byte)
    elif len(a_byte) > 8:
        return (-1)
    n_bytes = 0
    for i in a_byte:
        if i == '0':
            break
        n_bytes += 1
    # print(n_bytes)
    return (n_bytes)


def right_shift(num):
    # print((num >> 1) - 1)
    return ((num >> 1) - 1)


def validUTF8(data):
    i = 0
    t = False
    while (i < len(data)):
        if is_byte(data[i]):
            t = True
            i += 1
            continue
        else:
            n_bytes = many_bytes(data[i])
            if (n_bytes > 3) or (n_bytes == -1):
                return (False)
            # print(f"i am {n_bytes} bytes")
            # print("tried")
            if (i + n_bytes + 1) > len(data):
                # print('short')
                return (False)
            con_num = data[i: (i + n_bytes + 1)]
            j = 0
            while (j < len(con_num) - 1):
                j_cur = int(xtract(con_num[j]), 2)
                j_next = int(xtract(con_num[j + 1]), 2)
                # print(j_cur, j_next)
                if right_shift(j_cur) != j_next:
                    # print('shifting error')
                    return (False)
                j += 1
                t = True
            i = i + n_bytes + 1
    return (t)
