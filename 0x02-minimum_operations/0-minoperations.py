#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that calculates
the fewest number of operations needed to result in exactly n H characters in the file.
"""
from typing import List


def getFactors(n: int) -> List[int]:
    """
    Get the factors of a number and return a list.
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return factors

def minOperations(n: int) -> int:
    """
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste. Given a number n, write a method that calculates
    the fewest number of operations needed to result in exactly n H characters in the file.
    """
    if (n <= 0): return 0

    factors = getFactors(n)
    return sum(factors)
