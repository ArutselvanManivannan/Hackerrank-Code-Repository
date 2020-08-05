# https://www.hackerrank.com/challenges/python-time-delta/problem?

from datetime import datetime

for _ in range(int(input())):
    d1 = datetime.strptime(input(), "%a %d %b %Y %X %z")
    d2 = datetime.strptime(input(), "%a %d %b %Y %X %z")

    timeDelta = abs(d1 - d2)
    print(timeDelta.total_seconds())

# github.com/ArutselvanManivannan
