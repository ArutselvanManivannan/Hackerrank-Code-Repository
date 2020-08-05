# https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem

n = int(input())
x = [float(i) for i in input().split()]
y = [float(i) for i in input().split()]

x_mean = sum(x) / n
y_mean = sum(y) / n

std_x = (sum([(i - x_mean)**2 for i in x]) / n) ** 0.5
std_y = (sum([(i - y_mean)**2 for i in y]) / n) ** 0.5

p = (sum([(x[i] - x_mean) * (y[i] - y_mean) for i in range(n)])) / (n * std_x * std_y)

print(round(p, 3))
