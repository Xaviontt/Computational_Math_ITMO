import numpy as np
from scipy.misc import derivative


def check_interval(expression, start, end):
    if not expression(start) * expression(end) < 0:
        return False

    start_derivative_1 = derivative(expression, start, n=1)
    start_derivative_2 = derivative(expression, start, n=2)

    for i in np.arange(start, end, 0.01):
        if not ((start_derivative_1 * derivative(expression, i, n=1) > 0) and (
                start_derivative_2 * derivative(expression, i, n=2) >= 0)):
            print(f"Первая производная для начала = {start_derivative_1}, "
                  f"\nВторая производная для начала = {start_derivative_2}, "
                  f"\nПервая производная для {i} = {derivative(expression, i, n=1)} "
                  f"\nВторая производная для {i} = {derivative(expression, i, n=2)}")
            return False

    return True


def choose_x0(expression, start, end):
    start_derivative_2 = derivative(expression, start, n=2)
    print(f"Вторая производная от a = {start_derivative_2}, {expression(start)}")
    end_derivative_2 = derivative(expression, end, n=2)
    print(f"Вторая производная от b = {end_derivative_2}, {expression(end)}")

    if start_derivative_2 * expression(start) > 0:
        return start
    else:
        return end


def newton(expression, start, end, accuracy):
    if not check_interval(expression, start, end):
        return

    x0 = choose_x0(expression, start, end)
    # x0 = end
    # x0 = start
    print(f"Значение x0 = {x0}")
    x1 = x0 - expression(x0) / derivative(expression, x0, n=1)

    n = 0
    xi = x1
    xi_previous = x0
    while abs(xi - xi_previous) > accuracy:
        n += 1
        xi_previous = xi
        xi = xi - expression(xi) / derivative(expression, xi, n=1)

    return xi
