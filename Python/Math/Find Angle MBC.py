# https://www.hackerrank.com/challenges/find-angle/problem

import math

AB = int(input())
BC = int(input())

deg = math.degrees(math.atan(AB / BC))

print(f'{round(deg)}{chr(176)}')


# github.com/ArutselvanManivannan
