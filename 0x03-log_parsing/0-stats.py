#!/usr/bin/python3
import sys

def extract_metrics(line):
    # Define a dictionary to hold the status code counts
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    
    # Initialize variables for total file size and line count
    total_file_size = 0
    line_count = 0
    
    try:
        for line in sys.stdin:
            line_count += 1
            elements = line.split()
            
            # Check if the line matches the expected format
            if len(elements) >= 9:
                status_code = elements[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
                file_size = int(elements[-1])
                total_file_size += file_size

            # Print statistics every 10 lines or on keyboard interruption
            if line_count % 10 == 0:
                print(f"Total file size: {total_file_size}")
                for code in sorted(status_codes.keys()):
                    count = status_codes[code]
                    if count > 0:
                        print(f"{code}: {count}")

    except KeyboardInterrupt:
        pass  # Handle keyboard interruption gracefully

    finally:
        print(f"Total file size: {total_file_size}")
        for code in sorted(status_codes.keys()):
            count = status_codes[code]
            if count > 0:
                print(f"{code}: {count}")

if __name__ == '__main__':
    extract_metrics()
