# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

n = int(input())
contacts = {}
for i in range(n):
    a, b = input().split()
    contacts[a] = b

while True:
    try:
        name = input()
        if name in contacts:
            print('{}={}'.format(name, contacts[name]))
        else:
            print('Not found')
    except:
        break

# github.com/ArutselvanManivannan
