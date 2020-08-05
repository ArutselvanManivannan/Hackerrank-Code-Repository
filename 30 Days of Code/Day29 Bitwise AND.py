# https://www.hackerrank.com/challenges/30-bitwise-and/problem

for _ in range(int(input())):
    n, k = [int(i) for i in input().split()]
    print(k - 1 if ((k - 1) | k) <= n else k - 2)

# github.com/ArutselvanManivannan
