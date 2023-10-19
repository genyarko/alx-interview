#!/usr/bin/python3

import sys

total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

try:
    for line_number, line in enumerate(sys.stdin, start=1):
        elements = line.split()

        # Check if the line matches the expected format
        if len(elements) >= 9:
            status_code = elements[-2]
            file_size = int(elements[-1)

            # Update total file size
            total_size += file_size

            # Update status code count
            if status_code in status_codes:
                status_codes[status_code] += 1

        if line_number % 10 == 0:
            print(f"File size: {total_size}")
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    pass  # Handle keyboard interruption gracefully

finally:
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")
