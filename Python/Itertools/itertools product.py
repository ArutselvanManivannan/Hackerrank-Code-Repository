# https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

print(*list(product(a, b)))

# github.com/ArutselvanManivannan
