# https://www.hackerrank.com/challenges/30-sorting/problem

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

swaps = 0

while True:
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            swaps += 1
            break
    else:
        break

print(f'Array is sorted in {swaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')


# github.com/ArutselvanManivannan
