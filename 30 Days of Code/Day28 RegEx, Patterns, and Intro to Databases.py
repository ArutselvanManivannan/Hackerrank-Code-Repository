# https://www.hackerrank.com/challenges/30-regex-patterns/problem

import re

names = []

for _ in range(int(input())):
    name, email = input().split()
    if re.search(r'@gmail.com$', email):
        names.append(name)

print(*sorted(names), sep='\n')

# github.com/ArutselvanManivannan
