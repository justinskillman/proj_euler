# Euler Problem 2 #

n = 2
def fibb_sum(n, nold=1):
    global csum
    if n==2:
        csum = 0

    if n <= 4000000:
        if n % 2 == 0:
            csum = n + csum

        fibb_sum(n + nold, n)

    return csum
