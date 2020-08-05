# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy
numpy.set_printoptions(legacy='1.13')

n, m = [int(i) for i in input().split()]

arr = numpy.array([[int(i) for i in input().split()] for _ in range(n)])



print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(numpy.std(arr))


# github.com/ArutselvanManivannan
