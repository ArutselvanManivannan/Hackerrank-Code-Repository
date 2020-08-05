# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    count, index = 0, 0
    while True:
        index = string.find(sub_string, index)
        if index != -1:
            count += 1
            index += 1
        else:
            break

    return count

# github.com/ArutselvanManivannan
