# Euler Problem 5 #
import numpy as np

nums = np.array(xrange(1, 21))
minm = nums.prod()

succ = 0
maxjump = max(nums)
i = maxjump
while succ == 0:
    if len([x for x in nums if i % x == 0]) == len(nums):
        minm = i
        succ = 1
    i = i + maxjump
