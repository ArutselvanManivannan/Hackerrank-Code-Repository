# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

d = OrderedDict()
t = int(input())
for _ in range(t):
    key, value = input().rsplit(' ', 1)

    d[key] = d.get(key, 0) + int(value)

for key, value in d.items():
    print(key, value)

# github.com/ArutselvanManivannan
