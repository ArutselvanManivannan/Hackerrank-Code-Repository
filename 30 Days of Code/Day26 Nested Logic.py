# https://www.hackerrank.com/challenges/30-nested-logic/problem

rd, rm, ry = [int(i) for i in input().split()]
dd, dm, dy = [int(i) for i in input().split()]

if ry > dy:
    print('10000')
elif rm > dm and ry == dy:
    print(int((rm - dm) * 500))
elif rd >= dd and rm == dm and ry == dy:
    print(int((rd - dd) * 15))
else:
    print('0')

# github.com/ArutselvanManivannan
