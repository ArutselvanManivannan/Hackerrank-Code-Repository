# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

t = int(input())

markSheet = namedtuple('markSheet', input().split())

totalSum = 0

for _ in range(t):
    val1, val2, val3, val4 = input().split()
    data = markSheet(val1, val2, val3, val4)
    totalSum += int(data.MARKS)

print(f'{totalSum/t:.2f}')

# github/ArutselvanManivannan
