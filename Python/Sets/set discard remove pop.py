# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    op, *val = input().split()

    getattr(s, op)(*[int(v) for v in val])

print(sum(s))

# github.com/ArutselvanManivannan
