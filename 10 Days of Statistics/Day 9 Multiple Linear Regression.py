import numpy as np
from sklearn import linear_model

m, n = [int(i) for i in input().split()]
x, y = [], []
for _ in range(n):
    *a, b = [1] + [float(i) for i in input().split()]
    x.append(a)
    y.append(b)

# using sklearn
lm = linear_model.LinearRegression()
lm.fit(x, y)

a = lm.intercept_
b = lm.coef_

b = np.array([a, b[1], b[2]])

q = int(input())
for _ in range(q):
    x_var = [1] + [float(i) for i in input().split()]
    print(x_var @ b)


# without using sklearn

x, y = np.array(x), np.array(y)
xTranspose = np.transpose(x)

b = (np.linalg.inv(xTranspose @ x) @ xTranspose) @ y

q = int(input())
for _ in range(q):
    x_var = [1] + [float(i) for i in input().split()]
    print(x_var @ b)
