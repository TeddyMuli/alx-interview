#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that calculates
the fewest number of operations needed to result in exactly n H characters in the file.
"""
from typing import List


def get_factors(no_of_chars: int) -> List[int]:
    """
    Get the factors of a number and return a list.
    """
    factors = []
    while no_of_chars % 2 == 0:
        factors.append(2)
        no_of_chars //= 2

    for i in range(3, int(no_of_chars**0.5) + 1, 2):
        while no_of_chars % i == 0:
            factors.append(i)
            no_of_chars //= i

    if no_of_chars > 2:
        factors.append(no_of_chars)

    return factors

def minOperations(n: int) -> int:
    """
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n, write a method that calculates
    the fewest number of operations needed to result in exactly n H characters in the file.
    """
    if n <= 0:
        return 0

    factors = get_factors(n)
    return sum(factors)
