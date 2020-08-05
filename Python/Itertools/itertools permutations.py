# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

word, k = input().split()

p = sorted(list(permutations(word, int(k))))

for i in p:
    print(*i, sep='')


# github.com/ArutselvanManivannan
