# https://www.hackerrank.com/challenges/python-string-formatting/problem

import sys

sys.stdin = open("E:\\REC\\Hackerrank\\input.txt")
sys.stdout = open("E:\\REC\\Hackerrank\\output.txt", "w")


def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(str(i).rjust(width), end=' ')
        print(str(oct(i)[2:]).rjust(width), end=' ')
        print(str(hex(i)[2:]).upper().rjust(width), end=' ')
        print(str(bin(i)[2:]).rjust(width), end=' ')
        print()

# github.com/ArutselvanManivannan
