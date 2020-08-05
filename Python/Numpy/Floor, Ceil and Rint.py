# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy

numpy.set_printoptions(legacy='1.13')

arr = numpy.array([float(i) for i in input().split()])

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))


# github.com/ArutselvanManivannan
