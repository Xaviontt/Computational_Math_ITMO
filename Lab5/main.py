import numpy as np

from methods import *
from plot import *
from input import *


def main():
    data = getdata_input()
    x = np.array([dot[0] for dot in data['dots']])
    y = np.array([dot[1] for dot in data['dots']])

    plot_x = np.linspace(np.min(x), np.max(x), 100)
    plot_y = None

    if data['method_id'] == '1':
        answer = lagrange_polynomial(data['dots'], data['x'])
        plot_y = [lagrange_polynomial(data['dots'], x) for x in plot_x]
    elif data['method_id'] == '2':
        answer = newton_polynomial(data['dots'], data['x'])
        plot_y = [lagrange_polynomial(data['dots'], x) for x in plot_x]
    else:
        answer = None

    if answer is not None:
        plot(x, y, plot_x, plot_y)

    print(f"Приближенное значение функции: {answer}")


if __name__ == "__main__":
    main()
