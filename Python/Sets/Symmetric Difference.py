# https://www.hackerrank.com/challenges/symmetric-difference/problem

_, a = int(input()), set([int(i) for i in input().split()])
_, b = int(input()), set([int(i) for i in input().split()])


print(*sorted(a ^ b), sep='\n')


# github.com/ArutselvanManivannan
