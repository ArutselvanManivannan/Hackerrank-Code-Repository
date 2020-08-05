# https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product, starmap, repeat

k, m = [int(i) for i in input().split()]
k_arrs = []
for _ in range(k):
    f = [int(i) for i in input().split()]
    k_arrs.append(f[1:])

max_sum = 0

for prod in product(*k_arrs):
    prods = sum(list(map(pow, prod, repeat(2)))) % m

    if prods >= max_sum:
        max_sum = prods

print(max_sum)


# github.com/ArutselvanManivannan
