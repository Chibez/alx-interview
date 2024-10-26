#!/usr/bin/python3
"""
Log parsing
"""

import sys

if __name__ == '__main__':
    # Initialize variables
    filesize = 0
    count = 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {code: 0 for code in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """Print statistics in the required format."""
        print("File size: {}".format(file_size))
        for code in sorted(stats):
            if stats[code] > 0:
                print("{}: {}".format(code, stats[code]))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                # Extract status code and update its count
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except IndexError:
                continue  # Ignore lines that don't have enough data

            try:
                # Update total file size
                filesize += int(data[-1])
            except (IndexError, ValueError):
                continue  # Ignore lines where file size is not an integer

            # Print stats every 10 lines
            if count % 10 == 0:
                print_stats(stats, filesize)

        # Final stats output
        print_stats(stats, filesize)

    except KeyboardInterrupt:
        # Handle keyboard interruption gracefully
        print_stats(stats, filesize)
        raise
