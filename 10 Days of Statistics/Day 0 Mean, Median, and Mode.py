# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

import numpy as np
from scipy import stats


t = int(input())
a = [int(i) for i in input().split()]

print(np.mean(a))
print(np.median(a))
print(int(stats.mode(a)[0]))

# github.com/ArutselvanManivannan
