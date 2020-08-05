# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem

from math import sqrt, erf

mean, std = 2.4, 2.0

n = 100

mean, std = n * mean, sqrt(n) * std

def cdf(x): return 0.5 * (1 + erf((x - mean) / (std * sqrt(2))))
# cdf = lambda x: 0.5*(1 + erf((x - mean) / (std * sqrt(2))))


print(round(cdf(250), 4))

# github.com/ArutselvanManivannan
