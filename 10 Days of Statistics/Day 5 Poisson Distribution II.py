# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

meanA, meanB = 0.88, 1.55

costA = 160 + 40 * (meanA + meanA**2)
costB = 128 + 40 * (meanB + meanB**2)

print(round(costA, 3))
print(round(costB, 3))

# github.com/ArutselvanManivannan
