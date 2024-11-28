def func1(x, u):
    return u**2 + x


def func2(x, u):
    return u**3 +2 * x * u

def func3(x, u):
    if abs(x) > 1e154 or abs(u) > 1e154:
        raise OverflowError(f"Function input too large: x = {x}, u = {u}")
    return x**2 + u**2
