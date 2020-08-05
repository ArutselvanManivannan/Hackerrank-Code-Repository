# https://www.hackerrank.com/challenges/s10-weighted-mean/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
arr = list(map(int, input().split()))
weights = list(map(int, input().split()))

s = sum([arr[i] * weights[i] for i in range(t)])

print(f'{s/sum(weights):.1f}')


# using numpy
import numpy as np

weight_mean = np.average(arr, weights=weights)

print(weight_mean)

# github.com/ArutselvanManivannan
