#!/usr/bin/python3
import sys

def is_valid_log_line(line):
    # Check if the line matches the specified format
    return all([
        line.startswith('<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>'),
        line.count('"GET /projects/260 HTTP/1.1"') == 1
    ])

def print_statistics(total_file_size, status_code_counts):
    print(f'Total file size: {total_file_size}')
    for code in sorted(status_code_counts):
        count = status_code_counts[code]
        if count > 0:
            print(f'{code}: {count}')

def main():
    total_file_size = 0
    status_code_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if not is_valid_log_line(line):
                continue

            # Parse the line
            _, _, _, _, status_code, file_size = line.split()
            status_code = status_code.strip()
            file_size = int(file_size)

            # Update metrics
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_statistics(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        pass

    print_statistics(total_file_size, status_code_counts)

if __name__ == '__main__':
    main()
