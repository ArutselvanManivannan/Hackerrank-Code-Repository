# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem

from math import sqrt, erf

mean, std = 205, 15
n = 49

mean = mean * n
std = sqrt(n) * std

def cdf(x): return 0.5 * (1 + erf((x - mean) / (std * sqrt(2))))


print(round(cdf(9800), 4))


# github.com/ArutselvanManivannan
