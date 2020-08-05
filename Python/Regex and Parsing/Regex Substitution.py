# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

for _ in range(int(input())):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))


# github.com/ArutselvanManivannan
