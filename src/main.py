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


def find_lcm(x, y):
    return (x * y) // find_gcd(x, y)


def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def newton_coef(x, y):
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            a[i] = (a[i] - a[i - 1]) / (x[i] - x[i - j])

    return a


def main():
    x = [Fraction(-5), Fraction(-1), Fraction(0), Fraction(2)]
    y = [Fraction(-2), Fraction(6), Fraction(1), Fraction(3)]
    coef = newton_coef(x, y)
    print(coef)


if __name__ == '__main__':
    main()
