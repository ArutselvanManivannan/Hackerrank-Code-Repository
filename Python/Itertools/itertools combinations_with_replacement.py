# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

word, k = input().split()
word = sorted([w for w in word])

combinations = combinations_with_replacement(word, int(k))

print(*[''.join(com) for com in combinations], sep='\n')

# github.com/ArutselvanManivannan
