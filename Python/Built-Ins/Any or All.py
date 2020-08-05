# https: // www.hackerrank.com / challenges / any - or-all / problem

n = int(input())
arr = [int(i) for i in input().split()]

print(True if all(i >= 0 for i in arr) and any(str(i) == str(i)[::-1] for i in arr) else False)

# elaborate:
# if all(i >= 0 for i in arr) and any(str(i) == str(i)[::-1] for i in arr):
#     print(True)
# else:
#     print(False)


# github.com/ArutselvanManivannan
