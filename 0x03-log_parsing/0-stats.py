#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import sys
import re
import logging

class InvalidInputError(Exception):
    pass

def extract_input(input_line):
    '''
    Extracts sections of a line of an HTTP request log.

    Args:
        input_line (str): The input line to parse.

    Returns:
        dict: A dictionary containing the extracted information.
    '''
    log_format = re.compile(r'\s*(?P<ip>\S+)\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)]'
                            r'\s*"(?P<request>[^"]*)"\s*(?P<status_code>\S+)'
                            r'\s*(?P<file_size>\d+)')
    
    match = log_format.match(input_line)
    if not match:
        raise InvalidInputError(f"Invalid input line: {input_line}")
    
    return match.groupdict()

def print_statistics(total_file_size, status_codes_stats):
    '''
    Prints the accumulated statistics of the HTTP request log.

    Args:
        total_file_size (int): The total file size.
        status_codes_stats (dict): A dictionary of status codes and their counts.
    '''
    logging.info(f'Total file size: {total_file_size}')
    for code, count in sorted(status_codes_stats.items()):
        if count > 0:
            logging.info(f'{code}: {count}')

def update_metrics(line, total_file_size, status_codes_stats):
    '''
    Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): A dictionary of status codes and their counts.

    Returns:
        int: The new total file size.
    '''
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    return total_file_size + int(line_info['file_size'])

def run():
    '''
    Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run()
