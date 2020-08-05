# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    import string

    if size == 1:
        print('a')
        return

    s = string.ascii_lowercase
    # middle portion gives us the total width of the rangoli
    middle = '-'.join(s[size - 1:0:-1] + s[:size])
    rangoli_width = len(middle)

    ans = []

    for i in range(1, size):
        # curr has all the elements of the current row to be considered
        curr = s[size - 1:i:-1] + s[i:size]
        curr = '-'.join(curr)
        ans.append(curr.center(rangoli_width, '-'))

    print('\n'.join(ans[::-1]))
    print(middle)
    print('\n'.join(ans))


# github.com/ArutselvanManivannan
