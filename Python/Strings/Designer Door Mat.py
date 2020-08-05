# https://www.hackerrank.com/challenges/designer-door-mat/problem

n, m = [int(i) for i in input().split()]

s = 'WELCOME'
design = '.|.'

middle = s.center(m, '-')
# print(middle)

d = [pattern.center(m, '-') for pattern in [design * i for i in range(1, n, 2)]]

print(*d, sep='\n')
print(middle)
print(*d[::-1], sep='\n')


# github.com/ArutselvanManivannan
