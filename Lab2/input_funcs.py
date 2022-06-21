def read_expression():
    print("\nВыберите выражение:")
    print("1) x^3 - x + 4")
    print("2) x^3 + 2*x^2 + 3*x + 2.5")
    print("3) x^3 - 2")

    choose = int(input("$"))
    while (choose != 1) and (choose != 2) and (choose != 3):
        choose = int(input("$"))

    if choose == 1:
        expression = lambda x: x**3 - x + 4
    elif choose == 2:
        expression = lambda x: x**3 + 2 * x**2 + 3 * x + 2.5
    elif choose == 3:
        expression = lambda x: x**3 - 2

    return expression


def read_interval():
    print("\nВведите начало интервала")
    start = float(input('$'))
    print("Введите конец интервала")
    end = float(input('$'))

    if end <= start:
        print("Конец интервала должен быть больше, чем его начало, но ничего, поменяем")
        a = end
        end = start
        start = a
        return start, end
    else:
        return start, end


def read_accuracy():
    print("\nВведите точность:")
    return float(input('$'))


def read_method():
    print("\nВыберите метод решения:")
    print("1) Метод Ньютона")
    print("2) Метод секущих")
    print("3) Метод простой итерации")
    return int(input('$'))
