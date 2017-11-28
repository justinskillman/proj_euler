# Euler Problem 4 #

import math
import numpy as np

"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 X 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def IsPalin(n):

    """Determinens if a number, n, is a palindrome
    e.g. the same backwards as forwards."""

    letts = str(n)
    letts = list(letts)
    if len(letts) % 2 != 0:
        mid = len(letts)/2 + 1
        rev = letts[mid:]
        rev.reverse()
        same = True
        for i in xrange(len(rev)):
            if rev[i] != letts[i]:
                same = False
                break
        return same

    else:
        mid = len(letts)/2
        rev = letts[mid:]
        rev.reverse()
        same = True
        for i in xrange(len(rev)):
            if rev[i] != letts[i]:
                same = False
                break
        return same

def FindLrgPalin(ndigs):

    """Given the number of digits, ndigs, determines largest palindrome
    created by product of two ndigs-digit numbers."""

    maxn = (10 ** ndigs) - 1
    minn = (10 ** (ndigs - 1))
    i = maxn

    maxprod = 0

    while i >= minn:
        j = i
        while j >= minn:
            if IsPalin(i * j) and (i*j > maxprod):
                maxprod = i * j
                maxij = (i, j)
            j -= 1
        i -= 1

    print "The two ints are: " + str(maxij[0]) + " and " + str(maxij[1])
    print "Their product is: " + str(maxij[0]*maxij[1])
    return maxij[0]*maxij[1]

FindLrgPalin(3)
