# https://www.hackerrank.com/challenges/30-interfaces/problem

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        return sum([i for i in range(1, n//2 +1) if n%i == 0]) + n


# github.com/ArutselvanManivannan
