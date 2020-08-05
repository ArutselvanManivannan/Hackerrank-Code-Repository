# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem

def person_lister(f):
    def inner(people):
        # complete the function
        people = sorted(people, key=lambda x: int(x[2]))
        return (f(p) for p in people)
    return inner

# github.com/ArutselvanManivannan
