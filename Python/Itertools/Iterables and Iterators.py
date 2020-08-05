# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

import itertools

_ = int(input())

comb = list(itertools.combinations(input().split(), int(input())))
l = len(comb)
comb = [c for c in comb if 'a' in c]

print(len(comb) / l)

# github.com/ArutselvanManivannan
