# https://www.hackerrank.com/challenges/piling-up/problem


from collections import deque

for _ in range(int(input())):
    n = int(input())
    sideLength = deque([int(i) for i in input().split()])

    lastCube = pow(2, 31)

    while len(sideLength) > 1:
        if sideLength[0] >= sideLength[-1] and (sideLength[0] <= lastCube):
            lastCube = sideLength.popleft()
        elif sideLength[0] < sideLength[-1] and (sideLength[-1] <= lastCube):
            lastCube = sideLength.pop()
        else:
            print('No')
            break
    else:
        print('Yes')

# github.com/ArutselvanManivannan
