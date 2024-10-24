#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_counts = {}
line_count = 0
valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

# Function to print statistics
def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

# Signal handler for keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Set up signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
try:
    for line in sys.stdin:
        parts = line.split()

        # Validate format
        if len(parts) < 7 or not parts[5].startswith('"GET') or not parts[6].startswith('/projects/260'):
            continue

        try:
            # Extract status code and file size
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total size and status count
            total_size += file_size

            if status_code in valid_status_codes:
                if status_code not in status_counts:
                    status_counts[status_code] = 0
                status_counts[status_code] += 1

            line_count += 1

            # Print stats after every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            # Skip lines that don't match the expected format
            continue

# Handle keyboard interruption
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

