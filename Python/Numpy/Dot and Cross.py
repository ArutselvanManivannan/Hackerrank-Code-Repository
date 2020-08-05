# https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy

n = int(input())

a1 = numpy.array([[int(i) for i in input().split()] for _ in range(n)])
a2 = numpy.array([[int(i) for i in input().split()] for _ in range(n)])

print(a1 @ a2)
print(numpy.dot(a1, a2))
print(numpy.matmul(a1, a2))

# github.com/ArutselvanManivannan
