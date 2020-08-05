# https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

s = Counter(sorted(input()))

for i in s.most_common(3):
    print(*i)


# github.com/ArutselvanManivannan
