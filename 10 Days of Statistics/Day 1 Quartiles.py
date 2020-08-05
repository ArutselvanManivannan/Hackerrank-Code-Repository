# https://www.hackerrank.com/challenges/s10-quartiles/problem


n = int(input())
data = sorted(list(map(int, input().split())))


from statistics import median

print(int(median(data[:n // 2])))
print(int(median(data)))
print(int(median(data[(n + 1) // 2:])))


# or using quantiles directly
from statistics import quantiles

print(*[int(q) for q in quantiles(data)], sep='\n')

# github.com/ArutselvanManivannan
