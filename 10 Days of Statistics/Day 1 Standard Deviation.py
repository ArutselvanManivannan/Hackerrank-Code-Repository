# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

import math
from statistics import mean

n = int(input())
a = [int(i) for i in input().split()]

m = mean(a)

print(round(math.sqrt(sum([(i - m)**2 for i in a]) / n), 1))

# or
print(statistics.std(a))

# github.com/ArutselvanManivannan
