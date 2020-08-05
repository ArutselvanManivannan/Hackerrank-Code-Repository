# https://www.hackerrank.com/challenges/python-lists/problem

import sys

sys.stdin = open("E:\\REC\\Hackerrank\\input.txt")
sys.stdout = open("E:\\REC\\Hackerrank\\output.txt", "w")

n = int(input())
List = []
for _ in range(n):
    op, *val = input().split()
    if val:
        val = [int(i) for i in val]

    if op == 'print':
        print(List)
    else:
        getattr(List, op)(*val)


# github.com/ArutselvanManivannan
