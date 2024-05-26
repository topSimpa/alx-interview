#!/usr/bin/python3
"""
   Program does a log parsing
"""

import sys
import signal
import re

# set count to zero, file_sizes to [], status_code to {}
count = 0
file_sizes = []
interrupted = False
status_code = {}

# define the different regex and save them in variables
ip_address_regex = r'(((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9]))'
date_regex = r'(-\[\d{4}-\d{2}-\d{2}(2[0-3]|[0-1][0-9]):([0-5][0-9]):([0-5][0-9])\.\d{6}\])'
text_regex = r'("GET/projects/260HTTP/1.1")'
status_code_regex = r'(200|301|400|401|403|404|405|500)'
size_regex = r'(102[0-4]|10[01][0-9]|\d{3}|\d{2}|\d)'

# write a function collect: collect important details and store in
# File_sizes and status_code

# define a function that collects the line read from stdin


def collect(print_det):
    file_sizes.append(int(print_det[1]))
    if print_det[0] in status_code.keys():
        status_code[print_det[0]] += 1
    else:
        status_code[print_det[0]] = 1


# log_print: write function that prints as requested
def log_print():
    # orders status code
    # print(f'File size:  {sum(file_size)})
    print(f'File size: {sum(file_sizes)}')
    # Loop through the status_code and then print each key value pair in this
    # format
    for key, value in dict(sorted(status_code.items())).items():
        if value > 0:
            # print(f'{key}: {value}')
            print(f'{key}: {value}')


# define Signal handler
#def handler(signum, frame):
    # call  log_print
    # global interrupted
    # interrupted = True
    # try:
    #log_print()
    #sys.exit()
    # raise KeyboardInterrupt
    # except KeyboardInterrupt as e:
    #    print(e)
    # raise KeyboardInterruptt


# invoke signal handler
# signal.signal(signal.SIGINT, handler)
#signal.signal(signal.SIGINT, handler)
# print(e)
# print(handler)
# print(signal.getsignal(signal.SIGINT))
# start loop that reads stdin
try:
    for line in sys.stdin:
        if interrupted:
            print('true')
            # sys.exit(1)
            # if line matches format
        count += 1

        #print(line)
        line = line.split()
        #print(line)
        print_det = line[7: 9]
        #print(line)
        #print(print_det)
        line = ''.join(line)
        #print(line)
        #print(ip_address_regex + date_regex + text_regex + status_code_regex + size_regex)
        format_check = re.fullmatch(
            ip_address_regex +
            date_regex +
            text_regex +
            status_code_regex +
            size_regex,
            line)
        if (format_check):
            collect(print_det)
        else:
            continue
        #check if count is multiple of 10
        if count % 10 == 0:
            # call log_print
            log_print()
except Exception as e:
    pass
finally:
    log_print()
