#!/usr/bin/python3
import sys

# Initialize variables
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    line_number = 0

    for line in sys.stdin:
        line = line.strip()

        # Parse the line using a regular expression
        import re
        match = re.match(r'(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$', line)

        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            # Update total file size
            total_file_size += file_size

            # Update status code count
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        line_number += 1

        if line_number % 10 == 0:
            # Print statistics every 10 lines
            print(f"Total file size: {total_file_size}")
            for code in sorted(status_code_counts.keys()):
                count = status_code_counts[code]
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    pass  # Handle keyboard interruption gracefully

finally:
    # Print final statistics
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")
