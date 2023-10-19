#!/usr/bin/python3
import sys

# Initialize variables
total_size = 0
status_codes = {}

# Loop through stdin
for i, line in enumerate(sys.stdin):
    # Parse line
    try:
        ip, _, _, path, status_code, file_size = line.split()
        file_size = int(file_size)
        status_code = int(status_code)
    except ValueError:
        # Skip line if format is incorrect
        continue
    
    # Update total file size
    total_size += file_size
    
    # Update status code count
    if status_code in status_codes:
        status_codes[status_code] += 1
    else:
        status_codes[status_code] = 1
    
    # Print statistics every 10 lines or on keyboard interruption
    if (i + 1) % 10 == 0:
        print(f"Total file size: {total_size}")
        for code in sorted(status_codes.keys()):
            print(f"{code}: {status_codes[code]}")
    
    # Handle keyboard interruption
    try:
        sys.stdin.flush()
    except KeyboardInterrupt:
        print(f"Total file size: {total_size}")
        for code in sorted(status_codes.keys()):
            print(f"{code}: {status_codes[code]}")
        sys.exit(0)

# Print final statistics
print(f"Total file size: {total_size}")
for code in sorted(status_codes.keys()):
    print(f"{code}: {status_codes[code]}")
    
