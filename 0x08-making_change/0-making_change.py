#!/usr/bin/python3
""" Making change module
"""


def makeChange(coins, total):
    """ Determine the fewest number of coins needed to meet a given amount
    """
    if total <= 0:
        return 0

    min_coins = 0
    coins.sort(reverse=True)

    for coin in coins:
        if total % coin <= total:
            min_coins += total // coin
            total = total % coin
    return min_coins if total == 0 else -1
