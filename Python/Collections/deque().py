# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque

d = deque()

for _ in range(int(input())):
    query = input().split()
    if query[0] == 'append':
        d.append(int(query[1]))
    elif query[0] == 'appendleft':
        d.appendleft(int(query[1]))
    elif query[0] == 'pop':
        d.pop()
    else:
        d.popleft()

    # alternative
    # op, *num = input().split()

    # getattr(d, op)(*num)

print(*list(d))

# github.com/ArutselvanManivannan
