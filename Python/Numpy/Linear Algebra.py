# https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy

arr = numpy.array([[float(i) for i in input().split()] for _ in range(int(input()))])

print(round(numpy.linalg.det(arr), 2))

# github.com/ArutselvanManivannan
