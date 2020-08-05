# https://www.hackerrank.com/challenges/30-recursion/problem

def factorial(n):
    return 1 if n <= 1 else n*factorial(n-1)


print(factorial(int(input())))

# github.com/ArutselvanManivannan
