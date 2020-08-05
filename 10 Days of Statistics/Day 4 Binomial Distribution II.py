# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial

p, n = [int(i) for i in input().split()]


def binomial(x, n, p):
    nCr = factorial(n) / (factorial(n - x) * factorial(x))

    return nCr * pow(p, x) * pow(1 - p, n - x)


def output1():
    b = 0
    for i in range(3):
        b += binomial(i, 10, 0.12)

    return b


def output2():
    b = 0
    for i in range(2, 11):
        b += binomial(i, 10, 0.12)

    return b


print(round(output1(), 3))
print(round(output2(), 3))


# github.com/ArutselvanManivannan
