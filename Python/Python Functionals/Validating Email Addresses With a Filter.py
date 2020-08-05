# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

def fun(s):
    import re
    # return True if s is a valid email, else return False
    return bool(re.search(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s))

# github.com/ArutselvanManivannan
