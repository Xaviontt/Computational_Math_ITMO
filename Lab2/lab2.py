import matplotlib.pyplot as plt

from Anecdote_getter.anecdote_getter import *

from input_funcs import *

from method_newton import *
from method_simple_iteration import *
from method_secant import *


def main():
    # print("Хотите анекдот? (да/нет)")
    # anecdote = input("$")
    #
    # if anecdote == "да":
    #     get_anecdote()

    expression = read_expression()
    start, end = read_interval()
    accuracy = read_accuracy()

    match read_method():
        case 1:
            root = newton(expression, start, end, accuracy)
            if root is None:
                print("Неверный интервал и выражение для метода Ньютона")
            else:
                print(f"Значение функции = {expression(root)}")
                # print(f"Количество итераций = {n}")
                print(f"Корень = {root} на отрезке [{start}, {end}]")

                plt.plot([i for i in np.arange(start, end, 0.01)], [expression(i) for i in np.arange(start, end, 0.01)])
                plt.plot(root, expression(root), '*')
                plt.title(f"Корень на отрезке [{start},{end}]")
                plt.show()
            return

        case 2:
            root = secant(expression, start, end, accuracy)
            if root is None:
                print("Неверный интервал и выражение для метода секущих")
            else:
                print(f"Значение функции = {expression(root)}")
                # print(f"Количество итераций = {n}")
                print(f"Корень = {root} на отрезке [{start}, {end}]")

                plt.plot([i for i in np.arange(start, end, 0.01)], [expression(i) for i in np.arange(start, end, 0.01)])
                plt.plot(root, expression(root), '*')
                plt.title(f"Корень на отрезке [{start},{end}]")
                plt.show()
            return

        case 3:
            try:
                root = simple_iteration(expression, start, end, accuracy)
                if root is None:
                    print("Неверный интервал и выражение для метода простой итерации")
                else:
                    print(f"Значение функции = {expression(root)}")
                    # print(f"Количество итераций = {n}")
                    print(f"Корень = {root} на отрезке [{start}, {end}]")

                    plt.plot([i for i in np.arange(start, end, 0.01)], [expression(i) for i in np.arange(start, end, 0.01)])
                    plt.plot(root, expression(root), '*')
                    plt.title(f"Корень на отрезке [{start},{end}]")
                    plt.show()
                    return
            except TypeError:
                print("Неверный интервал и выражение для метода простой итерации")
                return


if __name__ == "__main__":
    main()

#Значение функции = -0.004032452062105563
#Корень = -1.7967863205826824 на отрезке [-2.0, 0.0]

#Значение функции = -0.0008292395179587686
#Корень = -1.7964174286105163 на отрезке [-2.0, 0.0]

#Значение функции = -0.022775077122096477
#Корень = -1.7989414021685552 на отрезке [-2.0, 0.0]