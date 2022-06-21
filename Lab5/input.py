from math import sin, sqrt


def getfunc(func_id):
    """ Получить выбранную функцию """
    if func_id == '1':
        return lambda x: sqrt(x)
    elif func_id == '2':
        return lambda x: x ** 2
    elif func_id == '3':
        return lambda x: sin(x)
    else:
        return None


def make_dots(f, a, b, n):
    dots = []

    h = (b - a) / (n - 1)
    for i in range(n):
        dots.append((a, f(a)))
        a += h

    return dots


def getdata_input():
    """ Получить данные с клавиатуры """
    data = {}

    print("\nВыберите метод интерполяции.")
    print(" 1 — Многочлен Лагранжа")
    print(" 2 — Многочлен Ньютона с конечными разностями")

    while True:
        try:
            method_id = input("Метод решения: ")
            if method_id != '1' and method_id != '2':
                raise AttributeError
            break
        except AttributeError:
            print("Метода нет в списке.")

    data['method_id'] = method_id

    print("\nВыберите способ ввода исходных данных.")
    print(" 1 — Набор точек")
    print(" 2 — Функция")

    while True:
        try:
            input_method_id = input("Способ: ")
            if input_method_id != '1' and input_method_id != '2':
                raise AttributeError
            break
        except AttributeError:
            print("Способа нет в списке.")

    dots = []

    if input_method_id == '1':
        print("Вводите координаты через пробел, каждая точка с новой строки.")
        print("Чтобы закончить, введите 'END'.")

        while True:
            try:
                current = input()
                if current == 'END':
                    if len(dots) < 2:
                        raise AttributeError
                    break
                x, y = map(float, current.split())
                dots.append((x, y))
            except ValueError:
                print("Введите точку повторно - координаты должны быть числами!")
            except AttributeError:
                print("Минимальное количество точек - две!")
    elif input_method_id == '2':
        print("\nВыберите функцию.")
        print(" 1 — √x")
        print(" 2 - x²")
        print(" 3 — sin(x)")

        while True:
            try:
                func_id = input("Функция: ")
                func = getfunc(func_id)
                if func is None:
                    raise AttributeError
                break
            except AttributeError:
                print("Функции нет в списке.")

        print("\nВведите через пробел границы отрезка.")
        while True:
            try:
                a, b = map(float, input("Границы отрезка: ").split())
                if a > b:
                    a, b = b, a
                break
            except ValueError:
                print("Границы отрезка должны быть числами, введенными через пробел.")

        print("\nВыберите количество узлов интерполяции.")
        while True:
            try:
                n = int(input("Количество узлов: "))
                if n < 2:
                    raise ValueError
                break
            except ValueError:
                print("Количество узлов должно быть целым числом > 1.")
        dots = make_dots(func, a, b, n)
    data['dots'] = dots

    print("\nВведите значение аргумента для интерполирования.")
    while True:
        try:
            x = float(input("Значение аргумента: "))
            break
        except ValueError:
            print("Значение аргумента должно быть числом.")
    data['x'] = x

    return data
