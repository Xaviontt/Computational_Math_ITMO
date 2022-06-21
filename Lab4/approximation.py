from math import log, exp
import numpy as np

from math_help import *


def lin_func(dots):
    """ Линейная аппроксимация """
    data = {}

    n = len(dots)
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]

    sx = sum(x)
    sx2 = sum([xi ** 2 for xi in x])
    sy = sum(y)
    sxy = sum([x[i] * y[i] for i in range(n)])

    d = solve_det([[sx2, sx], [sx, n]])
    d1 = solve_det([[sxy, sx], [sy, n]])
    d2 = solve_det([[sx2, sxy], [sx, sy]])

    try:
        a = d1 / d
        b = d2 / d
    except ZeroDivisionError:
        # print("Линейная аппроксимация невозможна")
        return None

    data['a'] = a
    data['b'] = b

    f = lambda z: a * z + b
    data['f'] = f

    data['str_f'] = "fi = ax + b"

    data['s'] = calc_s(dots, f)

    data['stdev'] = calc_stdev(dots, f)

    return data


def sqrt_func(dots):
    """ Квадратичная аппроксимация """
    data = {}

    n = len(dots)
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]

    sx = sum(x)
    sx2 = sum([xi ** 2 for xi in x])
    sx3 = sum([xi ** 3 for xi in x])
    sx4 = sum([xi ** 4 for xi in x])

    sy = sum(y)
    sxy = sum([x[i] * y[i] for i in range(n)])
    sx2y = sum([(x[i] ** 2) * y[i] for i in range(n)])

    d = solve_det([[n, sx, sx2],
                   [sx, sx2, sx3],
                   [sx2, sx3, sx4]])

    d1 = solve_det([[sy, sx, sx2],
                    [sxy, sx2, sx3],
                    [sx2y, sx3, sx4]])

    d2 = solve_det([[n, sy, sx2],
                    [sx, sxy, sx3],
                    [sx2, sx2y, sx4]])

    d3 = solve_det([[n, sx, sy],
                    [sx, sx2, sxy],
                    [sx2, sx3, sx2y]])

    try:
        c = d1 / d
        b = d2 / d
        a = d3 / d
    except ZeroDivisionError:
        # print("Квадратичная аппроксимация невозможна")
        return None

    data['c'] = c
    data['b'] = b
    data['a'] = a

    f = lambda z: a * (z ** 2) + b * z + c
    data['f'] = f

    data['str_f'] = "fi = ax^2 + bx + c"

    data['s'] = calc_s(dots, f)

    data['stdev'] = calc_stdev(dots, f)

    return data


def exp_func(dots):
    """ Экспоненциальная аппроксимация """
    data = {}

    n = len(dots)
    x = [dot[0] for dot in dots]
    y = []

    for dot in dots:
        if dot[1] <= 0:
            return None
        y.append(dot[1])

    lin_y = [log(y[i]) for i in range(n)]
    lin_result = lin_func([(x[i], lin_y[i]) for i in range(n)])

    a = exp(lin_result['b'])
    b = lin_result['a']
    data['a'] = a
    data['b'] = b

    f = lambda z: a * exp(b * z)
    data['f'] = f

    data['str_f'] = "fi = ae^(bx)"

    data['s'] = calc_s(dots, f)

    data['stdev'] = calc_stdev(dots, f)

    return data


def log_func(dots):
    """ Логарифмическая аппроксимация """
    data = {}

    n = len(dots)
    x = []
    for dot in dots:
        if dot[0] <= 0:
            return None
        x.append(dot[0])

    y = [dot[1] for dot in dots]

    lin_x = [log(x[i]) for i in range(n)]
    lin_result = lin_func([(lin_x[i], y[i]) for i in range(n)])

    a = lin_result['a']
    b = lin_result['b']
    data['a'] = a
    data['b'] = b

    f = lambda z: a * log(z) + b
    data['f'] = f

    data['str_f'] = "fi = a*ln(x) + b"

    data['s'] = calc_s(dots, f)

    data['stdev'] = calc_stdev(dots, f)

    return data


def pow_func(dots):
    """ Степенная аппроксимация """
    data = {}

    n = len(dots)
    x = []
    for dot in dots:
        if dot[0] <= 0:
            return None
        x.append(dot[0])
    y = []

    for dot in dots:
        if dot[1] <= 0:
            return None
        y.append(dot[1])

    lin_x = [log(x[i]) for i in range(n)]
    lin_y = [log(y[i]) for i in range(n)]
    lin_result = lin_func([(lin_x[i], lin_y[i]) for i in range(n)])

    a = exp(lin_result['b'])
    b = lin_result['a']
    data['a'] = a
    data['b'] = b

    f = lambda z: a * (z ** b)
    data['f'] = f

    data['str_f'] = "fi = ax^b"

    data['s'] = calc_s(dots, f)

    data['stdev'] = calc_stdev(dots, f)

    return data


def x3_func(dots):
    """ 3 аппроксимация """
    data = {}

    n = len(dots)
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    # print(n)

    sx = sum(x)
    sx2 = sum([xi ** 2 for xi in x])
    sx3 = sum([xi ** 3 for xi in x])
    sx4 = sum([xi ** 4 for xi in x])
    sx5 = sum([xi ** 5 for xi in x])
    sx6 = sum([xi ** 6 for xi in x])

    sy = sum(y)
    sxy = sum([x[i] * y[i] for i in range(n)])
    sx2y = sum([(x[i] ** 2) * y[i] for i in range(n)])
    sx3y = sum([(x[i] ** 3) * y[i] for i in range(n)])

    d = solve_det([[n, sx, sx2, sx3],
                   [sx, sx2, sx3, sx4],
                   [sx2, sx3, sx4, sx5],
                   [sx3, sx4, sx5, sx6]])

    d1 = solve_det([[sy, sx, sx2, sx3],
                    [sxy, sx2, sx3, sx4],
                    [sx2y, sx3, sx4, sx5],
                    [sx3y, sx4, sx5, sx6]])

    d2 = solve_det([[n, sy, sx2, sx3],
                    [sx, sxy, sx3, sx4],
                    [sx2, sx2y, sx4, sx5],
                    [sx3, sx3y, sx5, sx6]])

    d3 = solve_det([[n, sx, sy, sx3],
                    [sx, sx2, sxy, sx4],
                    [sx2, sx3, sx2y, sx5],
                    [sx3, sx4, sx3y, sx6]])

    d4 = solve_det([[n, sx, sx2, sy],
                    [sx, sx2, sx3, sxy],
                    [sx2, sx3, sx4, sx2y],
                    [sx3, sx4, sx5, sx3y]])

    m1 = np.array([[n, sx, sx2, sx3],
                   [sx, sx2, sx3, sx4],
                   [sx2, sx3, sx4, sx5],
                   [sx3, sx4, sx5, sx6]])

    v1 = np.array([sy, sxy, sx2y, sx3y])

    try:
        d = np.linalg.solve(m1, v1)[0]
        c = np.linalg.solve(m1, v1)[1]
        b = np.linalg.solve(m1, v1)[2]
        a = np.linalg.solve(m1, v1)[3]

    except ZeroDivisionError:
        return None
    data['c'] = c
    data['b'] = b
    data['a'] = a
    data['d'] = d

    f = lambda z: a * (z ** 3) + b * (z ** 2) + c * z + d
    data['f'] = f

    data['str_f'] = "fi = ax^3 + bx^2 + cx+d"

    data['s'] = calc_s(dots, f)
    # print(data['s'])

    data['stdev'] = calc_stdev(dots, f)
    # print(data['stdev'])

    return data
