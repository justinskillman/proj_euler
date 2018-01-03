# Euler Problem 7 #

import numpy as np

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13. What is the 10 001st prime number?
'''


def is_prime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


PrimesFnd = 0
j = -1
nthPrime = 10001

while PrimesFnd < nthPrime:
    j += 2
    if is_prime(j):
        PrimesFnd += 1

print str(j) + " is the " + str(nthPrime) + " prime!"


