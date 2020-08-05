# https://www.hackerrank.com/challenges/30-operators/problem

meal_cost = float(input())

tip_percent = int(input())

tax_percent = int(input())

answer = meal_cost + meal_cost * (tip_percent / 100) + meal_cost * (tax_percent / 100)
print(f'The total meal cost is {round(answer)} dollars.')


# github.com/ArutselvanManivannan
