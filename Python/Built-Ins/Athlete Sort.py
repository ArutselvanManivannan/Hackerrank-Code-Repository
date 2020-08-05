# https://www.hackerrank.com/challenges/python-sort-sort/problem


n, m = [int(i) for i in input().split()]

athletes = []

for _ in range(n):
    athletes.append([int(i) for i in input().split()])

k = int(input())

[print(*athlete) for athlete in sorted(athletes, key=lambda x: x[k])]

# github.com/ArutselvanManivannan
