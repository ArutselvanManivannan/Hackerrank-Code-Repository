# https://www.hackerrank.com/challenges/30-2d-arrays/problem

d = 6
array = []
for i in range(d):
    a = [int(i) for i in input().split()]
    array.append(a)
hour_glass = []
summation = 0

for i in range(4):
    for j in range(4):
        summation = summation + array[i][j] + array[i][j+1] + array[i][j+2] + array[i+1][j+1] + array[i+2][j] + array[i+2][j+1] + array[i+2][j+2]
        hour_glass.append(summation)
        summation = 0

print(max(hour_glass))


# github.com/ArutselvanManivannan
