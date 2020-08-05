# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem

from math import erf

mean, std = 20, 2
def cdf(x): return 0.5 * (1 + erf((x - mean) / (std * 1.414)))


print('{:.3f}'.format(cdf(19.5)))
print('{:.3f}'.format(cdf(22) - cdf(20)))


# github.com/ArutselvanManivannan
