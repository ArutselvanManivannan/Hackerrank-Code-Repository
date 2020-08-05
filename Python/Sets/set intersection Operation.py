# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

_, a = int(input()), set([int(i) for i in input().split()])
_, b = int(input()), set([int(i) for i in input().split()])

print(len(a.intersection(b)))

# github.com/ArutselvanManivannan
