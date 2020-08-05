# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

def wrapper(f):
    def fun(l):
        # complete the function
        number = [f'+91 {no[-10:-5]} {no[-5:]}' for no in l]
        return f(number)
    return fun

# github.com/ArutselvanManivannan
