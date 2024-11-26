import math


def analiticalTask1(u, h, n):
    x = []
    for i in range(n+1):
        x.append(3 * math.exp(u) - u ** 2 - 2 * u - 2)
        u += h
    return x


def analiticalTask2(x, h, n):
    res = []
    for i in range(n+1):
        res.append(math.exp(x ** 2) - (x ** 2) / 2 - 1 / 2)
        x += h
    return res
