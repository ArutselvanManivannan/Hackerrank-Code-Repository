# https://www.hackerrank.com/challenges/exceptions/problem

import sys

sys.stdin = open('E:\\REC\\Hackerrank\\input.txt')
sys.stdout = open('E:\\REC\\Hackerrank\\output.txt', 'w')

for _ in range(int(input())):
    try:
        a, b = [int(i) for i in input().split()]
        print(a // b)
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error Code: {e}")

# github.com/ArutselvanManivannan
