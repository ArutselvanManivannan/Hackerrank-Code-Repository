# https://www.hackerrank.com/challenges/re-start-re-end/problem

import sys

sys.stdin = open('E:\\REC\\Hackerrank\\input.txt')
sys.stdout = open('E:\\REC\\Hackerrank\\output.txt', 'w')

import re

s = input()
k = input()

pattern = re.compile(k)

search = pattern.search(s)

if not search:
    print(-1, -1)

i = 0

while search:
    print(f'({search.start()} {search.end() -1})')
    search = pattern.search(s, search.start() + 1)

# github.com/ArutselvanManivannan
