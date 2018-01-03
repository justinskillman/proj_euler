# Euler Problem 10 #

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import time

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

def sieve_eratosthenes(n):
    """Finds all primes less than some n"""
    sieve = range(2,n)

    j = sieve[0]
    while j < n:
        temp = [x for x in sieve if x <= j or x % j != 0]
        if len(temp) == len(sieve):
            return sieve
        else:
            sieve = temp

        j = sieve[sieve.index(j) + 1]


n = 2000000

t0 = time.time()
print(sum(filter(lambda x: is_prime(x) is True, range(2, n))))
t1 = time.time()
print str(t1 - t0)

t0 = time.time()
print(sum(sieve_eratosthenes(n)))
t1 = time.time()
print str(t1 - t0)
