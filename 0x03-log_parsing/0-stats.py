#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re

def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.
    '''
    log_pattern = re.compile(r'(?P<ip>\S+) - \[(?P<date>[\w\-\s:.]+)\] "(?P<request>[^"]*)" '
                            r'(?P<status_code>\d+) (?P<file_size>\d+)$')
    match = log_pattern.match(input_line)
    
    if match:
        return match.groupdict()
    
    return None

def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.
    '''
    print(f'File size: {total_file_size}')
    for code, count in sorted(status_codes_stats.items()):
        if count > 0:
            print(f'{code}: {count}')

def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    line_info = extract_input(line)
    if line_info:
        status_code = line_info['status_code']
        if status_code in status_codes_stats:
            status_codes_stats[status_code] += 1
        total_file_size += int(line_info['file_size'])
    return total_file_size

def run():
    '''Starts the log parser.
    '''
    total_file_size = 0
    status_codes_stats = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for line_num, line in enumerate(sys.stdin, start=1):
            total_file_size = update_metrics(line, total_file_size, status_codes_stats)

            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)

    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    import sys
    run()
