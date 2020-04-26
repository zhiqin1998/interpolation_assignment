from .math_lib import find_lcm, find_gcd


class Fraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if self.denominator != other.denominator:
            lcm = find_lcm(self.denominator, other.denominator)

            self_ratio = lcm // self.denominator
            other_ratio = lcm // other.denominator

            self_numerator = self.numerator * self_ratio
            other_numerator = other.numerator * other_ratio

            ans = Fraction(self_numerator + other_numerator, lcm)
            ans.simplify()

        else:
            ans = Fraction(self.numerator + other.numerator, self.denominator)

        return ans

    def __sub__(self, other):
        return self.__add__(-other)

    def __mul__(self, other):
        ans = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        ans.simplify()
        return ans

    def __truediv__(self, other):
        inv = Fraction(other.denominator, other.numerator)
        return self.__mul__(inv)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def simplify(self):
        gcd = find_gcd(self.numerator, self.denominator)
        if gcd != 1:
            self.numerator = self.numerator // gcd
            self.denominator = self.denominator // gcd

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return '{}/{}'.format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()
