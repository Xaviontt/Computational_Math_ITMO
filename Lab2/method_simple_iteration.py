import numpy as np
from scipy.misc import derivative


def find_lambda(expression, start, end):
    max_derivative = abs(derivative(expression, start, n=1))

    for i in np.arange(start, end, 0.01):
        if max_derivative < abs(derivative(expression, i, n=1)):
            max_derivative = abs(derivative(expression, i, n=1))

    return -1 / max_derivative


def simple_iteration(expression, start, end, accuracy):
    l = find_lambda(expression, start, end)
    phi = lambda x: x + expression(x) * l
    q = derivative(phi, start, n=1)

    print(q)

    x0 = start
    x1 = phi(x0)

    print(x1 - x0)

    criterion = lambda accuracy, x1, x0, q: abs(x1 - x0) > accuracy

    # print(f"Фи' от a = {derivative(phi, start, n=1)}")
    # print(f"Фи' от b = {derivative(phi, end, n=1)}\n")

    # xi = x1
    # xi_previous = x0

    # print(xi, " ", xi_previous)

    c = 0
    a = 0

    while (criterion(accuracy, x1, x0, q)):
        a = x1
        x1 = phi(x1)
        x0 = a

        c += 1

    return x1
