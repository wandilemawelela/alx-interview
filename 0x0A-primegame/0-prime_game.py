#!/usr/bin/python3
"""
This is the Prime Game module
"""


def isWinner(x, nums):
    if x == 0 or not nums:
        return None

    # Sieve of Eratosthenes to precompute prime numbers up to 10000
    MAX_N = 10000
    is_prime = [True] * (MAX_N + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    for start in range(2, int(MAX_N**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start*start, MAX_N + 1, start):
                is_prime[multiple] = False

    # Precompute results for every n from 1 to MAX_N
    prime_count = [0] * (MAX_N + 1)
    for i in range(1, MAX_N + 1):
        prime_count[i] = prime_count[i-1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
