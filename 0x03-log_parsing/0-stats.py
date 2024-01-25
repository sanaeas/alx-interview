#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""

import re


def extract(log_line):
    """Extract the status code and size from a log line"""
    fields = (
        r"\s*(?P<ip>\S+)\s*",
        r"\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]",
        r'\s*"(?P<request>[^"]*)"\s*',
        r"\s*(?P<status_code>\S+)",
        r"\s*(?P<file_size>\d+)"
    )

    info = {
        "status_code": 0,
        "file_size": 0,
    }

    log_format = "{}\\-{}{}{}{}\\s*".format(fields[0],
                                            fields[1],
                                            fields[2],
                                            fields[3],
                                            fields[4])
    resp_match = re.fullmatch(log_format, log_line)
    if resp_match is not None:
        status_code = resp_match.group("status_code")
        file_size = int(resp_match.group("file_size"))
        info["status_code"] = status_code
        info["file_size"] = file_size
    return info


def print_stats(total_size, status_stats):
    """Print the metrics for the log lines"""
    print("File size: {:d}".format(total_size), flush=True)
    for status_code in sorted(status_stats.keys()):
        num = status_stats.get(status_code, 0)
        if num > 0:
            print("{:s}: {:d}".format(status_code, num), flush=True)


def update_metrics(line, total_size, status_stats):
    """Updates the metrics"""
    line_info = extract(line)
    status_code = line_info.get("status_code", "0")
    if status_code in status_stats.keys():
        status_stats[status_code] += 1
    return total_size + line_info["file_size"]


def execute():
    """Start the log parsing"""
    line_num = 0
    total_size = 0
    status_stats = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    try:
        while True:
            line = input()
            total_size = update_metrics(
                line,
                total_size,
                status_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_stats(total_size, status_stats)
    except (KeyboardInterrupt, EOFError):
        print_stats(total_size, status_stats)


if __name__ == "__main__":
    execute()
