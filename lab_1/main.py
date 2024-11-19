from analitical import *
from euler import *
from func import *

def interfaceProgramm():
    stage = 0
    
	# x0 = 1
    # u0 = 0


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

    x = []
    n = int((b - a) / h)
    print(n)
    i = 0
    while True:
        if i != n + 1:
            x.append(a + h * i)
        else:
            break
        i += 1
        
    resultAnalitical = analiticalTask1(x[0], h , n)
    print(x)
    # print(resultAnalitical)
    
    resultEuler = eulerSolver(func1, 1, 0, n, h)
    
    print(resultEuler)
    





def stage2():
    pass


def stage3():
    pass


if __name__ == '__main__':
    interfaceProgramm()
