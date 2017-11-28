# Euler Problem 1 #

import math

tots = 1000
divs = [3, 5]

maxs = {x: tots/x - 1 for x in divs if tots % x == 0}
maxs.update({x: int(math.floor(tots/x)) for x in divs if tots % x != 0})

vec = [divs[0]*x for x in xrange(maxs[divs[0]] + 1)] + [divs[1]*x for x in xrange(maxs[divs[1]] + 1)]
print(sum(set(vec)))