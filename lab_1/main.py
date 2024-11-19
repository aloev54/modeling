def interfaceProgramm():
    stage = 0

    print("лабораторна работа №1")
    print("Выберите номер задания")
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
    n = (b - a) / h
    i = 0
    while True:
        if i != n + 1:
            x.append(a + h * i)
        else:
            break
        i += 1
    print(x)


def stage2():
    pass


def stage3():
    pass


if __name__ == '__main__':
    interfaceProgramm()
