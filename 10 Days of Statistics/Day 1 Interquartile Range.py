from statistics import median

n = int(input())
ele = [int(i) for i in input().split()]
freq = [int(i) for i in input().split()]

array = []

for i in range(n):
    array += [ele[i]] * freq[i]

array.sort()
n = len(array)

q1 = median(array[:n // 2])
q3 = median(array[(n + 1) // 2:])

# or
# from math import ceil
# from statistics import quantiles
# q1, q2, q3 = [ceil(i) for i in quantiles(array)]

print(f'{q3 - q1:.1f}')
