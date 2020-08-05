# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxzy'

findAll = re.findall(r'(?<=[' + consonants + '])([' + vowels + ']{2,})(?=[' + consonants + '])', input(), flags=re.I)


if findAll:
    [print(i) for i in findAll]
else:
    print(-1)


# github.com/ArutselvanManivannan
