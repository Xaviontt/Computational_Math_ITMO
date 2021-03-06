import traceback
from abc import ABC, abstractmethod

import numpy as np
from matplotlib import pyplot as plt
from tabulate import tabulate


class Method(ABC):
    def __init__(self):
        self.p = 0

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def solve(self, fun, reference_func, const_c, a, b, y0, h, e):
        pass

    def _print_table(self, dots, dots_h2, reference_func, const_c):
        try:
            all_acc_y = []
            tablet_solve = []

            for i in range(len(dots)):
                acc_y = reference_func(dots[i][0], const_c)
                all_acc_y.append(acc_y)
                tablet_solve.append([i, dots[i][0], dots[i][1], abs(acc_y - dots[i][1]), acc_y])
            print(tabulate(tablet_solve,
                           headers=['i', 'x', 'y(x)', 'Погрешность', 'Точное значение'],
                           tablefmt='fancy_grid', floatfmt='4.10f'
                           ))
            print()
            return True
        except Exception:
            print("Решения нет!")
            print()
            return False

    def draw_graph(self, dots, reference_func, const_c, a, b, ):
        try:
            plt.grid()

            x = np.array([dot[0] for dot in dots])
            y = np.array([dot[1] for dot in dots])

            acc_x = np.linspace(a, b, 100)
            acc_y = [reference_func(x, const_c) for x in acc_x]

            plt.title(self.get_name())
            plt.plot(x, y, '-o', color='b', label='численное решение')
            plt.plot(acc_x, acc_y, color='r', label='точное решение')
            plt.legend()
            plt.show()
            del x, y, acc_x, acc_y
        except ValueError:
            print(traceback.format_exc())
        except ZeroDivisionError:
            return
        except OverflowError:
            return


class EulerMethod(Method):
    def __init__(self):
        super().__init__()
        self.p = 2

    def get_name(self):
        return 'Метод Эйлера'

    def solve(self, fun, reference_func, const_c, a, b, y0, h, e):
        dots = self.process(fun, a, b, y0, h)
        dots_h2 = self.process(fun, a, b, y0, h / 2)
        if self._print_table(dots, dots_h2, reference_func, const_c):
            self.draw_graph(dots, reference_func, const_c, a, b)

    def process(self, fun, a, b, y0, h):
        dots = [(a, y0, fun(a, y0))]
        n = int((b - a) / h) + 1

        for i in range(1, n):
            try:
                x_prev = dots[i - 1][0]
                y_prev = dots[i - 1][1]
                y_cur = y_prev + h * (fun(x_prev, y_prev))
                x_cur = x_prev + h
                dots.append((x_cur, y_cur, fun(x_prev, y_prev)))
            except Exception:
                break
        return dots


class AdamsMethod(Method):
    def __init__(self):
        super().__init__()
        self.p = 4

    def get_name(self):
        return 'Метод Адамса'

    def solve(self, fun, reference_func, const_c, a, b, y0, h, e):
        dots = self.process(fun, a, b, y0, h, e)
        dots_h2 = self.process(fun, a, b, y0, h / 2, e)
        if self._print_table(dots, dots_h2, reference_func, const_c):
            self.draw_graph(dots, reference_func, const_c, a, b)

    def process(self, fun, a, b, y0, h, e):
        dots = [(a, y0)]
        fun_t = [fun(a, y0)]
        n = int((b - a) / h) + 1

        # Рунге-Кутта 4 порядка для нахождения 4 первых значений, чтобы запустить метод Адамса
        for i in range(1, 4):
            x_prev = dots[i - 1][0]
            y_prev = dots[i - 1][1]

            k1 = h * fun(x_prev, y_prev)
            k2 = h * fun(x_prev + h / 2, y_prev + k1 / 2)
            k3 = h * fun(x_prev + h / 2, y_prev + k2 / 2)
            k4 = h * fun(x_prev + h, y_prev + k3)

            x_cur = x_prev + h
            y_cur = y_prev + (k1 + 2 * k2 + 2 * k3 + k4) / 6

            dots.append((x_cur, y_cur))
            fun_t.append(fun(x_cur, y_cur))

        # Метод Адамса
        for i in range(4, n):
            try:
                x_cur = dots[i - 1][0] + h

                y_pred = dots[i - 1][1] + h / 24 * (55 * fun_t[i - 1] - 59 * fun_t[i - 2] + 37 * fun_t[i - 3] - 9 * fun_t[i - 4])

                fun_t.append(fun(x_cur, y_pred))

                y_cor = dots[i - 1][1] + h / 24 * (9 * fun_t[i] + 19 * fun_t[i - 1] - 5 * fun_t[i - 2] + fun_t[i - 3])

                while e < abs(y_cor - y_pred):
                        y_pred = y_cor
                        fun_t[i] = fun(x_cur, y_pred)
                        y_cor = dots[i - 1][1] + h / 24 * (9 * fun_t[i] + 19 * fun_t[i - 1] - 5 * fun_t[i - 2] + fun_t[i - 3])
            except Exception:
                break
            dots.append((x_cur, y_cor))

        return dots
