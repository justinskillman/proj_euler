# Euler Problem 12 #

import math

numdivs = 0
counter = 1

while numdivs < 500:
    target = sum(range(1, counter + 1))
    divs = [x for x in xrange(1, int(math.floor(math.sqrt(target)))) if target % x == 0]
    divs.extend([target / x for x in divs])
    divs = list(set(divs))

    numdivs = len(divs)
    counter += 1

print target


