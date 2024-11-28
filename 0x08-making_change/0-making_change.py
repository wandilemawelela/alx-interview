#!/usr/bin/python3
"""
The following module determines
the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """
    makeChange fucntion
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
