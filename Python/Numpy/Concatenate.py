# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy

array1, array2 = [], []

n, m, p = [int(i) for i in input().split()]

for _ in range(n):
    array1.append([int(i) for i in input().split()])

for _ in range(m):
    array2.append([int(i) for i in input().split()])

print(numpy.concatenate((array1, array2)))

# github.com/ArutselvanManivannan
