# https://www.hackerrank.com/challenges/no-idea/problem

n, m = [int(i) for i in input().split()]
array = [int(i) for i in input().split()]
a = set([int(i) for i in input().split()])
b = set([int(i) for i in input().split()])

happiness = 0

for i in array:
    if i in a:
        happiness += 1
    elif i in b:
        happiness -= 1

print(happiness)

# github.com/ArutselvanManivannan
