from method_newton import check_interval
from method_newton import choose_x0
from scipy.misc import derivative


def secant(expression, start, end, accuracy):
    if not check_interval(expression, start, end):
        return

    x0 = choose_x0(expression, start, end)
    x1 = x0 - expression(x0) / derivative(expression, x0, n=1)

    xi = x1
    xi_previous = x0

    n = 0
    while abs(xi - xi_previous) > accuracy:
        n += 1
        a = xi
        xi = xi - expression(xi) * (xi - xi_previous) / (expression(xi) - expression(xi_previous))
        xi_previous = a
    return xi
