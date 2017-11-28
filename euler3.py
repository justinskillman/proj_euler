# Euler Problem 3 #

import math


def isprime2(n):
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


target = 600851475143

divs = [x for x in xrange(3, int(math.floor(math.sqrt(target)))) if target % x == 0]
pdivs = [x for x in divs if isprime2(x)]
print(max(pdivs))
