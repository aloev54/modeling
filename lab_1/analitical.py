import math


def analiticalTask1(u, h, n):
    x = []
    for i in range(n+1):
        x.append(3 * math.exp(u) - u ** 2 - 2 * u - 2)
        u += h
    return x


def analiticalTask2(u, h, n):
    x = []
    for i in range(n+1):
        x.append(math.exp(u ** 2) - (u ** 2) / 2 - 1 / 2)
        u += h
    return x
