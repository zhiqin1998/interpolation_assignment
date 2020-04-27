import time

from src.fraction import Fraction


def evaluate(c, x, r):
    n = len(c) - 1
    temp = c[n]
    for i in range(n - 1, -1, -1):
        temp = temp * (r - x[i]) + c[i]
    return temp


def newton_coef(x, y):
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            a[i] = (a[i] - a[i - 1]) / (x[i] - x[i - j])

    return a


def parse(number):
    if number.count('/') == 1:
        number = number.split('/')
        return Fraction(int(number[0]), int(number[1]))
    elif '.' in number:
        number = number.split('.')
        numerator = int(''.join(number))
        denominator = 10 ** len(number[1])
        return Fraction(numerator, denominator)
    else:
        return Fraction(int(number))


def get_polynomial_str(c, x):
    # TODO create function to get string representation of polynomial
    pass


def main():
    xs = input('enter x values (separated by spaces): ').split()
    ys = input('enter y values (separated by spaces): ').split()
    assert len(xs) == len(ys)
    x = list(map(parse, xs))
    y = list(map(parse, ys))
    st = time.time()
    coef = newton_coef(x, y)
    print('time taken to calculate: {:.5f}ms'.format((time.time() - st) * 1000))
    print('coefficient of the newton polynomial is', ' '.join([str(c) for c in coef]))
    print('resulting polynomial is:')
    print(get_polynomial_str(coef, x))
    while True:
        r = input('enter value to interpolate at (q to exit): ')
        if r == 'q':
            break
        r = parse(r)
        st = time.time()
        ans = evaluate(coef, x, r)
        print('value at {} is {}'.format(r, ans))
        print('time taken to interpolate: {:.5f}ms'.format((time.time() - st) * 1000))


if __name__ == '__main__':
    main()
