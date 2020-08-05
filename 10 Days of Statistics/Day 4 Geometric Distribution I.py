# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
p = 1/3
n = 5

def geometric_distribution(n, p):
    return pow(1-p, n-1) * p

print(round(geometric_distribution(n, p), 3))

# github.com/ArutselvanManivannan
