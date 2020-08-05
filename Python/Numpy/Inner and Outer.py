# https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy

a = numpy.array([int(i) for i in input().split()])
b = numpy.array([int(i) for i in input().split()])

print(numpy.inner(a, b))
print(numpy.outer(a, b))

# github.com/ArutselvanManivannan
