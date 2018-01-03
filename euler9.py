# Euler Problem 9 #

import math
import itertools

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
maxn = 1000
minn = 1

for a, b in itertools.product(range(minn, maxn), range(minn, maxn)):
    c = math.sqrt(a ** 2 + b ** 2)
    if c > minn and a + b + c == maxn and c % 1 == 0:
        c = int(c)
        print "Conbination:", str(a), str(b), str(c)
        print "Product:", a*b*c
        break







