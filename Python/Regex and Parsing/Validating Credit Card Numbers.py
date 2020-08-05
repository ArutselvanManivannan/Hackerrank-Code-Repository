# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import sys

sys.stdin = open("E:\\REC\\Hackerrank\\input.txt")
sys.stdout = open("E:\\REC\\Hackerrank\\output.txt", "w")


import re

for _ in range(int(input())):
    cardno = input()
    if re.search(r'^[456](\d){15}$|^[456](\d){3}(-(\d){4}){3}$', cardno) and not re.search(r'(\d)\1\1\1', cardno.replace("-", "")):
        print('Valid')
    else:
        print('Invalid')



# github.com/ArutselvanManivannan
