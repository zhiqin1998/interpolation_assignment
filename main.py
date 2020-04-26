from src.fraction import Fraction


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
