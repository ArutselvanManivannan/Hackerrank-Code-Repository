# https://www.hackerrank.com/challenges/zipped/problem
n, m = [int(i) for i in input().split()]
marks = []
for _ in range(m):
    marks.append([float(i) for i in input().split()])

[print(sum(mark) / m) for mark in zip(*marks)]

# github.com/ArutselvanManivannan
