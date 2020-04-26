def find_lcm(x, y):
    return (x * y) // find_gcd(x, y)


def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x
