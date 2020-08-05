# https://www.hackerrank.com/challenges/polar-coordinates/problem


from math import sqrt
from cmath import phase

c = complex(input())

real, imag = c.real, c.imag

r = sqrt(real**2 + imag ** 2)
p = phase(c)

print(round(r, 3))
print(round(p, 3))

# github.com/ArutselvanManivannan
