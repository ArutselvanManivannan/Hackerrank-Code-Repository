# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

x = int(input())
stock = Counter([int(i) for i in input().split()])

earnings = 0

for _ in range(int(input())):
    size, price = [int(i) for i in input().split()]

    if stock[size]:
        earnings += price
        stock[size] -= 1

print(earnings)

# github.com/ArutselvanManivannan
