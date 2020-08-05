# https://www.hackerrank.com/challenges/re-group-groups/problem

import re

m = re.search(r'([0-9a-z])\1', input())
print(m.group(1) if m else -1)

# github.com/ArutselvanManivannan
