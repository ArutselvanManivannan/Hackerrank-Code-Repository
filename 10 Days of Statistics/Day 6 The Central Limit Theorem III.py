# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem

from math import sqrt

n = 100
mean = 500
std = 80
z = 1.96

sample_std = std / sqrt(n)
interval = sample_std * z

print(round(mean - interval, 2))
print(round(mean + interval, 2))

# github.com/ArutselvanManivannan
