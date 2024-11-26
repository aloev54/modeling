import math


def firstApproxTask1(u):
    return 1 + u + (u**3) / 3


def secondApproxTask1(u):
    return (u**4) / 12 + (u**3) / 3 + (u**2) / 2 + u + 1


def thirdApproxTask1(u):
    return (u**5) / 60 + (u**4) / 12 + (u**3) / 2 + (u**2) / 2 + u + 1


def forthApproxTask1(u):
    return (u**6) / 360 + (u**5) / 60 + (u**4) / 8 + (u**3) / 2 + (u**2) / 2 + u + 1


def firstApproxTask2(u):
    return 0.5 + (u**4) / 4 + (u**2) / 2

def secondApproxTask2(u):
    return 0.5 + (u**6)/12 + (u**4)/2 + (u**2)/2

def thirdApproxTask2(u):
    return 0.5 + (u**8)/48 + (u**6)/6 + (u**4)/2 + (u**2)/2


def forthApproxTask2(u):
    return 0.5 + (u**10)/240 + (u**8)/24 + (u**6)/6 + (u**4)/2 + (u**2)/2


def picarTask1(func, u0, h, n):
    res = []
    for i in range(n + 1):
        res.append(func(u0))
        u0 += h
    return res
