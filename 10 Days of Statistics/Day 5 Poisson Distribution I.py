# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

from math import factorial

k, mean = 5, 2.5


def poisson(k, mean):
    return (pow(mean, k) * pow(2.71828, -mean)) / factorial(k)


print(round(poisson(k, mean), 3))

# github.com/ArutselvanManivannan
