# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem

maxdepth = 0
def depth(elem, level):
    global maxdepth

    level += 1

    maxdepth = max(maxdepth, level)

    for child in elem:
        depth(child, level)

# github.com/ArutselvanManivannan
