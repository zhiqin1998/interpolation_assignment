from src.fraction import Fraction

def ceil(n):
    res = int(float(n))
    return res if res == float(n) or float(n) < 0 else res+1

def floor(n):
    res = int(float(n))
    return res if res == float(n) or float(n) >= 0 else res-1

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
        r = input('enter location to interpolate at (q to exit): ')
        if r == 'q':
            break
        # if(int(float(r))<len(x)-1 and int(float(r))>=0):
        #      val0 = x[floor(r)]
        #      val1 = x[ceil(r)]
        #      r = parse_loc(r, x)
        #      r = (val0.__add__(val1)).__mul__(r.__sub__(val0))
        # else:
        r = parse_loc(r, x)

        # print(r)

        if r is None:
            print('invalid location')
            continue
        ans = evaluate(coef, x, r)
        print('value at {} is {}'.format(r, ans))


if __name__ == '__main__':
    main()
