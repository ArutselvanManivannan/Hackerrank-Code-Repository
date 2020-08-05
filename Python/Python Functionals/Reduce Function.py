# https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-functionals

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

# github.com/ArutselvanManivannan
