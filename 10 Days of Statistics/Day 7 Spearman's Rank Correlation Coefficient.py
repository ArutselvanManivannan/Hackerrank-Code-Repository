# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem

n = int(input())
x = [float(i) for i in input().split()]
y = [float(i) for i in input().split()]

rank_x = {value: n - index for index, value in enumerate(sorted(x, reverse=True))}
rank_y = {value: n - index for index, value in enumerate(sorted(y, reverse=True))}

s = sum([(rank_x[x[i]] - rank_y[y[i]])**2 for i in range(n)])

ans = (6 * s) / (n * (n**2 - 1))
print(round(1 - ans, 3))
