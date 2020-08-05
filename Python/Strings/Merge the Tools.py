# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        s = string[i:i+k]
        new_s = {k:0 for k in s}
        print(''.join(list(new_s.keys())))


# github.com/ArutselvanManivannan
