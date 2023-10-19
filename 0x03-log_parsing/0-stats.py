#!/usr/bin/python3
import sys

def parse_log_line(line):
    """Parse a log line and return a tuple containing (status_code, file_size).
    Return (None, None) if the line does not match the expected format.
    """
    elements = line.split()
    if len(elements) >= 9:
        status_code = elements[-2]
        try:
            status_code = int(status_code)
            file_size = int(elements[-1])
            return status_code, file_size
        except ValueError:
            return None, None
    return None, None

def print_statistics(total_size, status_counts):
    """Print the accumulated statistics."""
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts.keys()):
        count = status_counts.get(code, 0)
        if count > 0:
            print(f"{code}: {count}")

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_log_line(line)
            
            if status_code is not None and status_code in status_counts:
                status_counts[status_code] += 1
                total_size += file_size
            
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
    
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
