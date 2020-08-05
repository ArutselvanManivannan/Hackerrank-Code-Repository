# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

import math


def isprime(n):
    if n == 2:
        return 'Prime'
    elif (n % 2) == 0 or n == 1:
        return 'Not prime'
    else:
        if all(n % x != 0 for x in range(3, int(math.sqrt(n) + 1), 2)):
            return 'Prime'
        else:
            return 'Not prime'


t = int(input())

for _ in range(t):
    a = int(input())
    print(isprime(a))

# github.com/ArutselvanManivannan
