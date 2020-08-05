# https://www.hackerrank.com/challenges/ginorts/problem


s = input()
digits = [int(i) for i in s if i.isdigit()]

print(*sorted([i for i in s if i.islower()]), sep='', end='')
print(*sorted([i for i in s if i.isupper()]), sep='', end='')
print(*sorted([str(i) for i in digits if i % 2 == 1]), sep='', end='')
print(*sorted([str(i) for i in digits if i % 2 == 0]), sep='', end='')

# or one liner

print(sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x)))

# github.com/ArutselvanManivannan
