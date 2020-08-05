# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        r = self.real + no.real
        i = self.imaginary + no.imaginary

        return Complex(r, i)

    def __sub__(self, no):
        r = self.real - no.real
        i = self.imaginary - no.imaginary

        return Complex(r, i)

    def __mul__(self, no):
        # (a+bi)*(c+di) = a*c + a*di + bi*c + bi*di
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary

        return Complex(a*c - b*d, a*d + b*c)

    def __truediv__(self, no):
        # https://arxiv.org/ftp/arxiv/papers/1608/1608.07596.pdf
        # alogirthm for real and imaginary parts in link
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary

        real_num = (a * c) + (b * d)
        imag_num = (b * c) - (a * d)

        denom = pow(c, 2) + pow(d, 2)

        return Complex(real_num/denom, imag_num/denom)

    def mod(self):
        return Complex(math.sqrt(pow(self.real, 2) + pow(self.imaginary, 2)), 0)


    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

# github.com/ArutselvanManivannan
