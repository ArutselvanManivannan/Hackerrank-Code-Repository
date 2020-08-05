# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy

n, m = [int(i) for i in input().split()]
arr = []

for _ in range(n):
    arr.append([int(i) for i in input().split()])

arr = numpy.array(arr)

print(numpy.transpose(arr))
print(arr.flatten())

# github.com/ArutselvanManivannan
