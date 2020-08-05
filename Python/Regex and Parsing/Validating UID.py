# https://www.hackerrank.com/challenges/validating-uid/problem

import re

for _ in range(int(input())):
    a = input()
    uppercase = re.findall(r'[A-Z]', a)
    digits = re.findall(r'\d', a)
    alphanum = re.findall(r'[a-zA-Z0-9]', a)
    repeat = re.findall(r'^.*(.).*(\1).*$', a)

    if len(uppercase) >= 2 and len(digits) >= 3 and len(alphanum) == 10 and not repeat:
        print('Valid')
    else:
        print('Invalid')
# github.com/ArutselvanManivannan
