# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby

for key, group in groupby(input()):
    print(f'({len(list(group))}, {key})', end=' ')

# github.com/ArutselvanManivannan
