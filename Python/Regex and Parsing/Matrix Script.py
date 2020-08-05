# https://www.hackerrank.com/challenges/matrix-script/problem

import sys

sys.stdin = open("E:\\REC\\Hackerrank\\input.txt")
sys.stdout = open("E:\\REC\\Hackerrank\\output.txt", "w")

import re

n, m = [int(i) for i in input().split()]
matrix = []
for _ in range(n):
    matrix.append(input())

decoded_matrix = ''
for i in range(0, m):
    try:
        for j in range(0, n):
            decoded_matrix += matrix[j][i]
    except:
        decoded_matrix += ''
        continue

print(decoded_matrix)

print(re.sub(r'(?<=[a-zA-Z])([!@#$%&\s])+(?=[a-zA-Z])', ' ', decoded_matrix))

# github.com/ArutselvanManivannan
