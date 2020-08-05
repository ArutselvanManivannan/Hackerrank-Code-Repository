# https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy

n, m = [int(i) for i in input().split()]

a1 = numpy.array([[int(i) for i in input().split()] for _ in range(n)])
a2 = numpy.array([[int(i) for i in input().split()] for _ in range(n)])

print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 // a2)
print(a1 % a2)
print(a1 ** a2)


# github.com/ArutselvanManivannan
