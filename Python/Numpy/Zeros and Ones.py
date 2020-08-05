# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy

dimensions = tuple([int(i) for i in input().split()])

print(numpy.zeros(dimensions, dtype=numpy.int))
print(numpy.ones(dimensions, dtype=numpy.int))


# github.com/ArutselvanManivannan
