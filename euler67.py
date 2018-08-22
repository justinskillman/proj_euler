# Euler Problem 67 #
import numpy as np

with open('p067_triangle.txt', 'r') as myfile:
    pyr=myfile.read()

pyr = pyr.rstrip()
pyr_lst = [x.split(' ') for x in pyr.split('\n')]
pyr_lst = [[int(y) for y in x] for x in pyr_lst]
max_n = np.max([len(x) for x in pyr_lst])
pyr_arr = np.vstack([np.array(x + [0] * (max_n - len(x))) for x in pyr_lst])

def eval_cell(parent, child_l, child_r):
    return parent + max(child_l, child_r)

def find_max(pyr_arr):
    # Solutions so we can use dynamic programming
    sols = np.empty(pyr_arr.shape)
    sols.fill(np.nan)
    sols[sols.shape[0]-1, :] = pyr_arr[sols.shape[0]-1,:]

    # Loop over cells
    for jRow in range(sols.shape[0]-2, -1, -1):
        for jCol in range(0, jRow+1):
            sols[jRow, jCol] = eval_cell(pyr_arr[jRow, jCol],
                                         sols[jRow+1, jCol],
                                         sols[jRow+1, jCol+1])
    return sols[0,0]

print(find_max(pyr_arr))
