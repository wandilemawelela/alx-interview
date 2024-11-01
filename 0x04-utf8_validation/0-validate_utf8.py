#!/usr/bin/python3
"""
This module determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    # Helper function to count the number of leading 1s in a byte
    def count_leading_ones(byte):
        count = 0
        for i in range(8):
            if (byte & (1 << (7 - i))) != 0:
                count += 1
            else:
                break
        return count

    i = 0
    n = len(data)

    while i < n:
        # Count the leading ones to determine the number
        # of bytes in the current character
        leading_ones = count_leading_ones(data[i])

        # Single byte character (ASCII)
        if leading_ones == 0:
            i += 1
            continue

        # For multi-byte characters, ensure the count is between 2 and 4
        if leading_ones == 1 or leading_ones > 4:
            return False

        # Check that the subsequent bytes start with '10'
        for j in range(1, leading_ones):
            if i + j >= n:
                return False
            if (data[i + j] & 0xC0) != 0x80:
                return False

        i += leading_ones

    return True
