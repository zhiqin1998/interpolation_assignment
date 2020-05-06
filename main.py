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


def parse_loc(number, x):
    if '.' in number:
        left, right = number.split('.')
        idx = int(left)
        frac = parse('0.{}'.format(right))
    else:
        idx = int(eval(number))
        frac = parse(number) - Fraction(idx)
    if idx < 0 or idx >= len(x) - 1:
        return None
    return x[idx] + (x[idx + 1] - x[idx]) * frac


def get_polynomial_str(c, x, frac=True):
    ans = []
    for i in range(len(c)):
        if frac:
            curr = str(c[i])
        else:
            curr = str(c[i].eval())
        if curr == '0':
            continue
        for j in range(i):
            if frac:
                t = str(x[j])
            else:
                t = str(x[j].eval())

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
    print('\ncoefficient of the newton polynomial is', ' '.join([str(c) for c in coef]))
    print('resulting polynomial is:')
    print(get_polynomial_str(coef, x))
    print('resulting polynomial (in decimal) is:')
    print(get_polynomial_str(coef, x, frac=False))
    while True:
        r = input('\nenter location to interpolate at (q to exit): ')
        if r == 'q':
            break
        r = parse_loc(r, x)
        if r is None:
            print('invalid location')
            continue
        ans = evaluate(coef, x, r)
        print('value at {} is {}'.format(r, ans))
        print('value at {} is {}'.format(r.eval(), ans.eval()))


if __name__ == '__main__':
    main()
