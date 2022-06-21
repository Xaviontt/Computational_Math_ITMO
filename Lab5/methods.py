from math import factorial


def lagrange_polynomial(dots, x):
    """ Многочлен Лагранжа """
    result = 0

    n = len(dots)
    for i in range(n):
        c1 = c2 = 1
        for j in range(n):
            if i != j:
                c1 *= x - dots[j][0]
                c2 *= dots[i][0] - dots[j][0]
        result += dots[i][1] * c1 / c2

    return result


def t_calc(t, n, forward=True):
    """ Вычислить параметр 't' для многочлена Ньютона """
    result = t

    for i in range(1, n):
        if forward:
            result *= t - i
        else:
            result *= t + i

    return result


def newton_polynomial(dots, x):
    """ Многочлен Ньютона с конечными разностями """
    n = len(dots)
    h = dots[1][0] - dots[0][0]
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        a[i][0] = dots[i][1]

    for i in range(1, n):
        for j in range(n - i):
            a[j][i] = a[j + 1][i - 1] - a[j][i - 1]

    if x <= dots[n // 2][0]:
        # Первая интерполяционная формула Ньютона
        x0 = n - 1
        for i in range(n):
            if x <= dots[i][0]:
                x0 = i - 1
                break
        if x0 < 0:
            x0 = 0
        t = (x - dots[x0][0]) / h

        result = a[x0][0]
        for i in range(1, n):
            result += (t_calc(t, i) * a[x0][i]) / factorial(i)
    else:
        # Вторая интерполяционная формула Ньютона
        t = (x - dots[n - 1][0]) / h

        result = a[n - 1][0]

        for i in range(1, n):
            result += (t_calc(t, i, False) * a[n - i - 1][i]) / factorial(i)

    return result
