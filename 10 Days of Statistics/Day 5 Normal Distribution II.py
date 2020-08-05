# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

from math import erf

mean, std = 70, 10

def cdf(x): return 0.5 * (1 + erf((x - mean) / (std * (2 ** 0.5))))


print(round((1 - cdf(80)) * 100, 2))
print(round((1 - cdf(60)) * 100, 2))
print(round(cdf(60) * 100, 2))

# github.com/ArutselvanManivannan

# for more info:
# https://docs.python.org/3/library/statistics.html#statistics.NormalDist
