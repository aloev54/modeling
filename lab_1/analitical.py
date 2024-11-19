import math


def analiticalTask1(x, h, n):
    res = []
    for i in range(n):
        res.append(3 * math.exp(x) - x ** 2 - 2 * x - 2)
        x += h
    return res


def analiticalTask2(x, h, n):
    res = []
    for i in range(n):
        res.append(math.exp(x ** 2) - (x ** 2) / 2 - 1 / 2)
        x += h
    return res
