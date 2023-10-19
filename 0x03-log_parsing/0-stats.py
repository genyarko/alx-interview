#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import fileinput
import os

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_count = 0

try:
    for line in fileinput.input():
        line_count += 1
        if line_count % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")
        try:
            ip, _, _, request, status, size = line.split()
            if request.startswith("GET /projects/260 HTTP/1.1") and status.isdigit():
                status = int(status)
                if status in status_codes:
                    status_codes[status] += 1
                total_size += int(size)
        except ValueError:
            pass
except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
