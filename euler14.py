# Euler Problem 14 #

# Parameters
bigN = 1000000

# Functions
def gen_collatz_seq(n):
    seq = [n]
    while n != 1:
        if (n % 2) == 0: # is even
            n = n / 2
            seq.append(n)
        else:
            n = 3*n + 1
            seq.append(n)
    return seq


# Main
maxl = 0
maxn = 0
for j in range(1, bigN):
    l = len(gen_collatz_seq(j))
    if l > maxl:
        print(j)
        maxl = l
        maxn = j

print(maxn)

