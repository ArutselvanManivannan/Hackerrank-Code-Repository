# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    # your code goes here
    kevin, stuart = 0, 0
    vowels = 'AEIOU'
    l = len(string)
    for i in range(l):
        if string[i] in vowels:
            kevin += (l - i)
        else:
            stuart += (l - i)

    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print(f'Kevin {kevin}')
    else:
        print(f'Stuart {stuart}')

# github.com/ArutselvanManivannan
