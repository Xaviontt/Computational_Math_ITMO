import math
from collections import namedtuple
from typing import Tuple

from methods import AdamsMethod, EulerMethod

Hint = namedtuple('Hint', ['a', 'b', 'y0', 'h', 'e'])
Function = namedtuple('Function', ['desc', 'func', 'reference', 'calc_const', 'hint'])

functions = [
    Function(
        'y` = y + (1 + x) * y^2',
        lambda x, y: y + (1 + x) * y ** 2,
        lambda x, c: - math.e ** x / (x * math.e ** x + (math.e - math.e)),
        lambda x0, y0: -math.e ** x0 / y0 - x0 * math.e ** x0,
        Hint(1, 2, -1, 0.05, 0.01),
    ),
    Function(
        'y` = (x + 1)^3 - y',
        lambda x, y: (x + 1) ** 3 - y,
        lambda x, c: c * math.e ** (-x) + x ** 3 + 3 * x - 2,
        lambda x0, y0: (y0 - x0 ** 3 - 3 * x0 + 2) * math.e ** x0,
        Hint(0, 3, 0, 0.1, 0.0001),
    ),
    Function(
        'y` = xy',
        lambda x, y: x * y,
        lambda x, c: c * math.e ** (x ** 2 / 2),
        lambda x0, y0: y0 / (math.e ** (x0 ** 2 / 2)),
        Hint(-1, 1, 1, 0.05, 0.0001),
    ),
]

methods = [
    EulerMethod(),
    AdamsMethod(),
]


def get_func():
    while True:
        try:
            print('Выберите уравнение для задачи Коши:')
            for i, f in enumerate(functions, 1):
                print(f'{i}. {f.desc}')
            func = functions[int(input()) - 1]
            return func
        except Exception:
            print("Неверный ввод. Попробуйте снова!")
            print()
            continue


def get_interval(func):
    while True:
        try:
            a, b = map(float, input(f'Введите интервал [a; b] ({func.hint.a} {func.hint.b}): ').split())
            return a, b
        except Exception:
            print("Неверный ввод. Попробуйте снова!")
            print()
            continue


def get_start_conditions(func):
    while True:
        try:
            y0 = float(input(f'Введите начальные условия y0 ({func.hint.y0}): '))
            return y0
        except Exception:
            print("Неверный ввод. Попробуйте снова!")
            print()
            continue


def get_step(func):
    while True:
        try:
            h = float(input(f'Введите шаг дифференцирования ({func.hint.h}): '))
            return h
        except Exception:
            print("Неверный ввод. Попробуйте снова!")
            print()
            continue


def get_acc(func):
    while True:
        try:
            e = float(input(f'Введите точность e ({func.hint.e}): '))
            return e
        except Exception:
            print("Неверный ввод. Попробуйте снова!")
            print()
            continue


def initialization() -> Tuple[Function, float, float, float, float, float]:
    func = get_func()
    a, b = get_interval(func)
    y0 = get_start_conditions(func)
    h = get_step(func)
    e = get_acc(func)
    return func, a, b, y0, h, e


def main():
    func, a, b, y0, h, e = initialization()

    for method in methods:
        print('Решение задачи Коши методом:', method.get_name())
        method.solve(
            func.func,
            func.reference,
            func.calc_const(a, y0),
            a,
            b,
            y0,
            h,
            e,
        )
        print()


if __name__ == "__main__":
    main()
