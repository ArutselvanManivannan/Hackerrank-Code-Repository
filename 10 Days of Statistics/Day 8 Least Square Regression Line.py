# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]

x_sum, y_sum = sum(x), sum(y)
xy_sum = sum([x[i] * y[i] for i in range(5)])
x_sqsum = sum([i**2 for i in x])

x_mean = x_sum / 5
y_mean = y_sum / 5

b = ((5 * xy_sum) - ((x_sum) * (y_sum))) / ((5 * x_sqsum) - (x_sum)**2)
a = y_mean - (b * x_mean)

x = 80
yCap = a + b * x

print(round(yCap, 3))
