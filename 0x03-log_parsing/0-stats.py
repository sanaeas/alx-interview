#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""

import re
import sys


LOG_PATTERN = (r"^(\S+) ?"
               r"- ?\[\S+ ?\S+\] "
               r"\"GET /projects/260 HTTP/1\.1\" "
               r"(\S+) (\S+)$")


def extract(log_line):
    """Extract the status code and size from a log line"""
    match = re.search(LOG_PATTERN, log_line)

    if match:
        return (match.group(2), match.group(3))
    else:
        return None, None


def print_stats(size, codes):
    """Print the metrics for the log lines read so far"""
    print("File size: {}".format(str(size)))
    for code in sorted(codes.keys()):
        if codes[code] != 0:
            print("{}: {}".format(code, str(codes[code])))


status_codes = {
    "200": 0, "301": 0,
    "400": 0, "401": 0,
    "403": 0, "404": 0,
    "405": 0, "500": 0
}
size = 0
lines = 0

try:
    for line in sys.stdin:
        lines += 1

        code, size = extract(line.strip())
        if code and size:
            try:
                size += int(size)
            except Exception:
                pass
            try:
                if code in status_codes:
                    status_codes[code] += 1
            except Exception:
                pass

        if lines % 10 == 0 and lines != 0:
            print_stats(size, status_codes)
except KeyboardInterrupt:
    pass

finally:
    print_stats(size, status_codes)
