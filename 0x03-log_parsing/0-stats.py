#!/usr/bin/python3
"""Solution to interview exercise
 0x03-log_parsing"""

import sys
import re

ip_address_regex = r'(((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9]))'
date_regex = r'(-\[\d{4}-\d{2}-\d{2}(2[0-3]|[0-1][0-9]):([0-5][0-9]):([0-5][0-9])\.\d{6}\])'
text_regex = r'("GET/projects/260HTTP/1.1")'
status_code_regex = r'(200|301|400|401|403|404|405|500)'
size_regex = r'(102[0-4]|10[01][0-9]|\d{3}|\d{2}|\d{1})'


count = 0
total_size = 0
status_code_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0}


def print_stats():
    print(f"File size: {total_size}")
    for key in status_code_count.keys():
        if status_code_count[key] > 0:
            print(f"{key}: {status_code_count[key]}")


try:
    for line in sys.stdin:
        line = line.strip()
        field_list = line.split()
        line = ''.join(field_list)
        format_check = re.fullmatch(
            ip_address_regex +
            date_regex +
            text_regex +
            status_code_regex +
            size_regex,
            line)
        if (format_check):
            [status, size] = field_list[7:]
            total_size += int(size)
            status_code_count[status] += 1
            count += 1
        if count == 10:
            count = 0
            print_stats()
except KeyboardInterrupt:
    count = 0
    print_stats()
    sys.exit(0)
