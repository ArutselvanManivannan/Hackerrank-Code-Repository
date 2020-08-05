# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy

n, m = [int(i) for i in input().split()]
arr = numpy.array([[int(i) for i in input().split()] for _ in range(n)])

sum = numpy.sum(arr, axis=0)
product = numpy.product(sum)

print(product)


# github.com/ArutselvanManivannan
