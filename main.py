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
    if '/' in number:
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
    ans = []
    for i in range(len(c)):
        curr = str(c[i])
        if curr == '0':
            continue
        for j in range(i):
            t = str(x[j])
            if t == '0':
                curr += '(x)'
            elif '-' in t:
                curr += '(x + {})'.format(t.replace('-', ''))
            else:
                curr += '(x - {})'.format(t)
        ans.append(curr)
    return ' + '.join(ans)


def main():
    xs = input('enter x values (separated by commas): ').split(',')
    ys = input('enter y values (separated by commas): ').split(',')
    assert len(xs) == len(ys)
    x = list(map(parse, xs))
    y = list(map(parse, ys))
    coef = newton_coef(x, y)
    print('coefficient of the newton polynomial is', ' '.join([str(c) for c in coef]))
    print('resulting polynomial is:')
    print(get_polynomial_str(coef, x))
    while True:
        r = input('enter value to interpolate at (q to exit): ')
        if r == 'q':
            break
        r = parse(r)
        ans = evaluate(coef, x, r)
        print('value at {} is {}'.format(r, ans))


if __name__ == '__main__':
    main()
