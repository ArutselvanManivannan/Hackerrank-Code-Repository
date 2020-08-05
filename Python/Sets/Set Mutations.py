# https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
s = set([int(i) for i in input().split()])
for _ in range(int(input())):
    op, size = input().split()
    values = set([int(i) for i in input().split()])

    getattr(s, op)(values)

print(sum(s))


# github.com/ArutselvanManivannan
