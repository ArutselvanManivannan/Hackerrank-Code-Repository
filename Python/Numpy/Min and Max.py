# https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy

n, m = [int(i) for i in input().split()]

arr = numpy.array([[int(i) for i in input().split()] for _ in range(n)])

m = numpy.min(arr, axis=1)
print(numpy.max(m))

# github.com/ArutselvanManivannan
