#!/usr/bin/python3

"""
Log parsing
"""

import sys
import signal
import re

# Initialize counters and storage
total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regular expression pattern to match the required log line format
log_pattern = re.compile(r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')


def print_stats():
    """Prints the current statistics (total file size and status code counts)."""
    global total_size, status_count
    print(f"File size: {total_size}")
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interrupt (Ctrl + C) to print stats."""
    print_stats()
    sys.exit(0)

# Register the signal handler for Ctrl + C
signal.signal(signal.SIGINT, signal_handler)


def process_line(line):
    """Processes a single log line and updates metrics if the line matches the format."""
    global total_size, line_count
    match = log_pattern.match(line)
    if match:
        # Extract status code and file size
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        # Update total size
        total_size += file_size

        # Update status code count if it's one of the defined codes
        if status_code in status_count:
            status_count[status_code] += 1

        # Increment the line count
        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()


if __name__ == "__main__":
    # Read stdin line by line
    try:
        for line in sys.stdin:
            process_line(line)
    except KeyboardInterrupt:
        # Print the final stats in case of an interruption
        print_stats()
        sys.exit(0)

    # Print final stats when all lines are processed
    print_stats()

