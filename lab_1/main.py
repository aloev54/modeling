#   Сводка по сделанной работе:
#   1)Реализова 1 задача (аналитический метод, Эйлер, Пикар1, Пикар2, Пикар3, Пикар4)
#   2)Реализова 2 задача (аналитический метод, Эйлер, Пикар1, Пикар2, Пикар3, Пикар4)
#

from analitical import *
from euler import *
from func import *
from picar import *
from helper import *



def interfaceProgramm():
    stage = 0

    print("лабораторна работа №1")
    print("Выберите номер задания")
    print("1 - задача 1, 2 - задача 2, 3 - задача 3")

    stage = int(input())

    if stage == 1:
        stage1()
    elif stage == 2:
        stage2()
    elif stage == 3:
        pass
    elif stage == 228:
        stage3()


def stage1():
    print("Программа № 1")
    print("a - начало интервала, b - конец интервала, h - шаг интервала")
    print("Начало интервала должно начинаться с 0 так как аналитический метод считается не тривиально!")

    print("Введите значение a")
    a = float(input())

    print("Введите значение b")
    b = float(input())

    print("Введите значение h")
    h = float(input())

    u0 = 0
    x0 = 1
    u = []
    n = int((b - a) / h)

    i = 0
    while True:
        if i != n + 1:
            u.append(a + h * i)
        else:
            break
        i += 1
    print(u)
    resultAnalitical = analiticalTask1(u[u0], h, n)

    resultEuler = eulerSolver(func1, x0, u0, n, h)

    resultPicar1 = picarTask1(firstApproxTask1, u0, h, n)

    resultPicar2 = picarTask1(secondApproxTask1, u0, h, n)

    resultPicar3 = picarTask1(thirdApproxTask1, u0, h, n)

    resultPicar4 = picarTask1(forthApproxTask1, u0, h, n)

    clearPrint(u, resultAnalitical, resultEuler, resultPicar1, resultPicar2, resultPicar3, resultPicar4)
    
    print()
    print("сходимость методов:")
    print("Вывод значения U до которого наблюдается полная сходимость")
    print("Пикар1 U = ", getdiff(u, resultPicar1, resultAnalitical))
    print("Пикар2 U = ", getdiff(u, resultPicar2, resultAnalitical))
    print("Пикар3 U = ", getdiff(u, resultPicar3, resultAnalitical))
    print("Пикар4 U = ", getdiff(u, resultPicar4, resultAnalitical))


def stage2():
    print("Программа № 2")
    print("a - начало интервала, b - конец интервала, h - шаг интервала")

    print("Введите значение a")
    a = float(input())

    print("Введите значение b")
    b = float(input())

    print("Введите значение h")
    h = float(input())

    u0 = 0
    x0 = 0.5
    u = []
    n = int((b - a) / h)
    # print(n)
    i = 0
    while True:
        if i != n + 1:
            u.append(a + h * i)
        else:
            break
        i += 1
    print(u)
    resultAnalitical = analiticalTask2(u[u0], h, n)

    resultEuler = eulerSolver(func2, x0, u0, n, h)

    resultPicar1 = picarTask1(firstApproxTask2, u0, h, n)

    resultPicar2 = picarTask1(secondApproxTask2, u0, h, n)

    resultPicar3 = picarTask1(thirdApproxTask2, u0, h, n)

    resultPicar4 = picarTask1(forthApproxTask2, u0, h, n)

    clearPrint(u, resultAnalitical, resultEuler, resultPicar1, resultPicar2, resultPicar3, resultPicar4)

    print()
    print("сходимость методов:")
    print("Вывод значения U до которого наблюдается полная сходимость")
    print("Пикар1 U = ", getdiff(u, resultPicar1, resultAnalitical))
    print("Пикар2 U = ", getdiff(u, resultPicar2, resultAnalitical))
    print("Пикар3 U = ", getdiff(u, resultPicar3, resultAnalitical))
    print("Пикар4 U = ", getdiff(u, resultPicar4, resultAnalitical))

def stage3():
    print("Программа № 3")
    print("a - начало интервала, b - конец интервала, h - шаг интервала")

    print("Введите значение a")
    a = float(input())

    print("Введите значение b")
    b = float(input())

    print("Введите значение h")
    h = float(input())

    u0 = 0
    x0 = 0
    u = []
    n = int((b - a) / h)
    # print(n)
    i = 0
    while True:
        if i != n + 1:
            u.append(a + h * i)
        else:
            break
        i += 1
    # print(u)

    resultEuler = eulerSolver(func3, u0, x0, n, h)

    resultPicar1 = picarTask1(firstApproxTask3, x0, h, n)

    resultPicar2 = picarTask1(secondApproxTask3, x0, h, n)

    resultPicar3 = picarTask1(thirdApproxTask3, x0, h, n)

    resultPicar4 = picarTask1(forthApproxTask3, x0, h, n)

    clearPrint(u, [], resultEuler, resultPicar1, resultPicar2, resultPicar3, resultPicar4)

    # print()
    # print("сходимость методов:")
    # print("Вывод значения U до которого наблюдается полная сходимость")
    # print("Пикар1 U = ", getdiff(u, resultPicar1, resultAnalitical))
    # print("Пикар2 U = ", getdiff(u, resultPicar2, resultAnalitical))
    # print("Пикар3 U = ", getdiff(u, resultPicar3, resultAnalitical))
    # print("Пикар4 U = ", getdiff(u, resultPicar4, resultAnalitical))


def clearPrint(u, analitical, euler, picar1, picar2, picar3, picar4):
    file = open ("out.txt", "w")
    for i in range(len(u)):
        if analitical != []:
            print("u =", round(u[i], 2), "\t", "anal= ", round(analitical[i], 2), "\t", "euler= ", round(euler[i], 2), "\t",
              "picar1= ", round(picar1[i], 2), "\t", "picar2= ", round(picar2[i], 2), "\t", "picar3= ",
              round(picar3[i], 2), "\t", "picar4= ", round(picar4[i], 2))
        else:
            print("u =", round(u[i], 2), "\t", "anal= - \t", "euler= ", round(euler[i], 2), "\t",
              "picar1= ", round(picar1[i], 2), "\t", "picar2= ", round(picar2[i], 2), "\t", "picar3= ",
              round(picar3[i], 2), "\t", "picar4= ", round(picar4[i], 2))

def clearPrint1(u, analitical, euler, picar1, picar2, picar3, picar4):
    file = open ("out.txt", "w")
    for i in range(len(u)):
        if analitical != []:
            print("u =", round(u[i], 2), "\t", "anal= ", round(analitical[i], 2), "\t", "euler= ", round(euler[i], 2), "\t",
              "picar1= ", round(picar1[i], 2), "\t", "picar2= ", round(picar2[i], 2), "\t", "picar3= ",
              round(picar3[i], 2), "\t", "picar4= ", round(picar4[i], 2))
        else:
            print("u =", round(u[i], 2), "\t", "anal= - \t", "euler= ", round(euler[i], 2), "\t",
              "picar1= ", round(picar1[i], 2), "\t", "picar2= ", round(picar2[i], 2), "\t", "picar3= ",
              round(picar3[i], 2), "\t", "picar4= ", round(picar4[i], 2))


if __name__ == '__main__':
    interfaceProgramm()
