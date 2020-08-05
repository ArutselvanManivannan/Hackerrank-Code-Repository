# https://www.hackerrank.com/challenges/py-check-subset/problem

for _ in range(int(input())):
    _, a = int(input()), set([int(i) for i in input().split()])
    _, b = int(input()), set([int(i) for i in input().split()])

    print(a.issubset(b))


# github.com/ArutselvanManivannan
