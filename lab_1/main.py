from analitical import *
from euler import *
from func import *
from picar import *


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
        stage3()


def stage1():
    print("Программа № 1")
    print("a - начало интервала, b - конец интервала, h - шаг интервала")

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
    # print(n)
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

def stage3():
    pass


def clearPrint(u, analitical, euler, picar1, picar2, picar3, picar4):
    for i in range(len(u)):
        print("u =", round(u[i], 2), "\t", "anal= ", round(analitical[i], 2), "\t", "euler= ", round(euler[i], 2), "\t",
              "picar1= ", round(picar1[i], 2), "\t", "picar2= ", round(picar2[i], 2), "\t", "picar3= ",
              round(picar3[i], 2), "\t", "picar4= ", round(picar4[i], 2))


if __name__ == '__main__':
    interfaceProgramm()
