# https://www.hackerrank.com/challenges/30-inheritance/problem

class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        self.avg = sum(self.scores) / len(self.scores)
        if self.avg >= 90 and self.avg <= 100:
            return 'O'
        elif self.avg >= 80 and self.avg < 90:
            return 'E'
        elif self.avg >= 70 and self.avg < 80:
            return 'A'
        elif self.avg >= 55 and self.avg < 70:
            return 'P'
        elif self.avg >= 40 and self.avg < 55:
            return 'D'
        else:
            return 'T'


# github.com/ArutselvanManivannan
