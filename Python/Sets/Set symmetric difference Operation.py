# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

_, a = int(input()), set([int(i) for i in input().split()])
_, b = int(input()), set([int(i) for i in input().split()])

print(len(a ^ b))

# github.com/ArutselvanManivannan
