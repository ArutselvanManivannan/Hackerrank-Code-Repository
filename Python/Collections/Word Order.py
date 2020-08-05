# https://www.hackerrank.com/challenges/word-order/problem


from collections import OrderedDict

d = OrderedDict()

for _ in range(int(input())):
    string = input().strip()
    d[string] = d.get(string, 0) + 1

print(len(d))
print(*list(d.values()))

# or

from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


d = OrderedCounter([input() for _ in range(int(input()))])

print(len(d))
print(*d.values())


# github.com/ArutselvanManivannan
