import math


def firstApproxTask1(u):
    return 1 + u + (u**3) / 3


def secondApproxTask1(u):
    return (u**4) / 12 + (u**3) / 3 + (u**2) / 2 + u + 1


def thirdApproxTask1(u):
    return (u**5) / 60 + (u**4) / 12 + (u**3) / 2 + (u**2) / 2 + u + 1


def forthApproxTask1(u):
    return (u**6) / 360 + (u**5) / 60 + (u**4) / 8 + (u**3) / 2 + (u**2) / 2 + u + 1

#------------------------Задание 1--------------------


def firstApproxTask2(u):
    return 0.5 + (u**4) / 4 + (u**2) / 2

def secondApproxTask2(u):
    return 0.5 + (u**6)/12 + (u**4)/2 + (u**2)/2

def thirdApproxTask2(u):
    return 0.5 + (u**8)/48 + (u**6)/6 + (u**4)/2 + (u**2)/2


def forthApproxTask2(u):
    return 0.5 + (u**10)/240 + (u**8)/24 + (u**6)/6 + (u**4)/2 + (u**2)/2

#------------------------Задание 2-------------------------

def firstApproxTask3(x):
    return (x**3)/3

def secondApproxTask3(x):
    return (x**3)/3 + (x**7)/21

def thirdApproxTask3(x):
    return  (x**3)/3 + (x**7)/63 + (2*(x**11))/693 + (x**15)/6615


def forthApproxTask3(x):
    return (x**3)/3 + (x**7)/63 + (2*(x**11))/2079 + (19*(x**15))/130977 + (2 * (x**19))/ 197505 + (2 * (x**23))/9585135 + (4*(x**27))/123773265 + (4*(x**23))/(23*693**2) + (x**31)/(31*6615**2)

#------------------------Задание 3-------------------------

def picarTask1(func, u0, h, n):
    res = []
    for i in range(n + 1):
        res.append(func(u0))
        u0 += h
    return res
