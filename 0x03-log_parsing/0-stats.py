#!/usr/bin/python3
import sys
import re

# Initialize variables to keep track of total file size and counts of status codes
total_size = 0
count = 0
status_code_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

# Regular expression patterns for the expected log format components
ip_address_regex = r'(((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9]))'
date_regex = r'(-\[\d{4}-\d{2}-\d{2}(2[0-3]|[0-1][0-9]):([0-5][0-9]):([0-5][0-9])\.\d{6}\])'
text_regex = r'("GET/projects/260HTTP/1.1")'
status_code_regex = r'(200|301|400|401|403|404|405|500)'
size_regex = r'(102[0-4]|10[01][0-9]|\d{3}|\d{2}|\d{1})'


def print_stats():
    """
    Function to print the current statistics.
    """
    print(f"File size: {total_size}")
    for key in sorted(status_code_count.keys()):
        if status_code_count[key] > 0:
            print(f"{key}: {status_code_count[key]}")

try:
    for line in sys.stdin:
        line = line.strip()
        fields = line.split()
        line = ''.join(fields)
        # Regex pattern to match the entire line format
        match = re.match(
            rf"^{ip_address_regex}{date_regex}{text_regex}{status_code_regex}{size_regex}$", line
        )

        if match:
            # Extract status code and file size from the matched groups
            [status, size] = [match.group(10), match.group(11)]

            # Update total size and count for the matched status code
            total_size += int(size)
            if status in status_code_count:
                status_code_count[status] += 1

            count += 1

        # Print statistics every 10 lines
        if count == 10:
            print_stats()
            count = 0

except KeyboardInterrupt:
    # Print statistics upon keyboard interruption (CTRL + C)
    print_stats()
    sys.exit(0)

# Print final statistics when EOF is reached
print_stats()

