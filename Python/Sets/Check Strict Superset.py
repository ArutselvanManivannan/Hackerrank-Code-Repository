# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

s = set([int(i) for i in input().split()])
for _ in range(int(input())):
    ss = set([int(i) for i in input().split()])
    if not ss.issubset(s) or len(s - ss) == 0:
        print(False)
        break
else:
    print(True)

# github.com/ArutselvanManivannan
