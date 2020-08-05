# https://www.hackerrank.com/challenges/nested-list/problem

import sys

sys.stdin = open("E:\\REC\\Hackerrank\\input.txt")
sys.stdout = open("E:\\REC\\Hackerrank\\output.txt", "w")


if __name__ == '__main__':
    marksheet = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())

        if not score in marksheet:
            marksheet[score] = [name]
        else:
            marksheet[score].append(name)

    marksheet = {key: value for key, value in sorted(marksheet.items())}
    print(*sorted(list(marksheet.values())[1]), sep='\n')

# github.com/ArutselvanManivannan
