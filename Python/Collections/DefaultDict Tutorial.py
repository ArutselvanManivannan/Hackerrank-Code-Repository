# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

d = defaultdict(list)

n, m = [int(i) for i in input().split()]
for _ in range(1, n + 1):
    d[input()].append(i)

for _ in range(m):
    a = input()
    for key, value in d.items():
        if a == key:
            print(*value)
            break
    else:
        print(-1)

# github.com/ArutselvanManivannan
