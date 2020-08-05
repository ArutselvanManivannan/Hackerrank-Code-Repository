# https://www.hackerrank.com/challenges/hex-color-code/problem

import re

pattern = re.compile(r'(?<!^)(#[0-9a-f]{6}|#[0-9a-f]{3})', re.I)

for _ in range(int(input())):
    m = pattern.findall(input())
    if m:
        for code in m:
            print(code)


# github.com/ArutselvanManivannan
