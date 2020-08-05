# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem


import re
import email.utils

for _ in range(int(input())):
    parser = email.utils.parseaddr(input())

    m = re.match(r'^[a-z][\w\._-]+@[a-zA-Z]+\.[a-z]{1,3}$', parser[1])

    if m:
        print(email.utils.formataddr(parser))

# github.com/ArutselvanManivannan
