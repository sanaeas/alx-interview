#!/usr/bin/python3
""" Prime Game
"""


def primeNumbers(n):
    """ Generate prime numbers up to 'n'
    """
    primes = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primes.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primes


def isWinner(x, nums):
    """ Determine the winner of a series of games played
    based on the number of prime numbers
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    maria_wins = ben_wins = 0
    for i in range(x):
        primes = primeNumbers(nums[i])
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
