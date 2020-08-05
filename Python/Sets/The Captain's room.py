# https://www.hackerrank.com/challenges/py-the-captains-room/problem

n = int(input())
rooms = [int(i) for i in input().split()]

room_a = set()
room_b = set()

for room in rooms:
    if room not in room_a:
        room_a.add(room)
    else:
        room_b.add(room)

print(*room_a - room_b)


# github.com/ArutselvanManivannan
