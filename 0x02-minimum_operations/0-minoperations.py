#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """
    Calculate the fewest number of operations
    needed to result in exactly n 'H' characters in the file.

    :param n: Target number of 'H' characters
    :type n: int
    :return: Minimum number of operations to
    achieve n 'H' characters
    :rtype: int
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
