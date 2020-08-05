# https://www.hackerrank.com/challenges/py-set-union/problem

_, a = int(input()), set([int(i) for i in input().split()])
_, b = int(input()), set([int(i) for i in input().split()])


print(len(a.union(b)))

# or
a.update(b)
print(len(a))

# github.com/ArutselvanManivannan
