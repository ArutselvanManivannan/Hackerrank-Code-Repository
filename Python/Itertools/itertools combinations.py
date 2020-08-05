# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

word, k = input().split()
word = sorted([w for w in word])

for i in range(1, int(k)+1):
    for j in combinations(word, i):
        print(''.join(j))

# github.com/ArutselvanManivannan
