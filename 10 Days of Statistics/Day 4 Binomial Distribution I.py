# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial

boy, girl = [float(i) for i in input().split()]

def binomial(x, n, p):
    comb = factorial(n) / (factorial(n-x) * factorial(x))

    return comb * (p**x) * ((1-p)**(n-x))

b, p, n = 0, 1.09/2.09, 6

for i in range(3, 7):
    b += binomial(i, n, p)

print(round(b, 3))

# github.com/ArutselvanManivannan
