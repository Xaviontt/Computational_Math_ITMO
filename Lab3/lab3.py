import math


class Integral:
    sum = 0.0
    nseg = 1  # число отрезков разбиения
    ncalls = 0  # считает число вызовов интегрируемой функции

    def restart(func, x0, x1, nseg0, reset_calls=True):
        if reset_calls:
            Integral.ncalls = 0
        Integral.nseg = nseg0
        # вычисление суммы для метода трапеций с начальным числом отрезков разбиения nseg0
        Integral.sum = 0.5 * (func(x0) + func(x1))
        dx = 1.0 * (x1 - x0) / nseg0
        for i in range(1, nseg0):
            Integral.sum += func(x0 + i * dx)

        Integral.ncalls += 1 + nseg0
        return Integral.sum * dx

    def double_nseg(func, x0, x1):
        nseg = Integral.nseg
        dx = (x1 - x0) / nseg
        x = x0 + 0.5 * dx
        i = 0
        AddedSum = 0.0
        for i in range(nseg):
            AddedSum += func(x + i * dx)

        Integral.sum += AddedSum
        Integral.nseg *= 2
        Integral.ncalls += nseg
        return Integral.sum * 0.5 * dx

    def trapezoid(func, x0, x1, rtol=1e-10, nseg0=1):
        ans = Integral.restart(func, x0, x1, nseg0)
        old_ans = 0.0
        err_est = max(1, abs(ans))
        while err_est > abs(rtol * ans):
            old_ans = ans
            ans = Integral.double_nseg(func, x0, x1)
            err_est = abs(old_ans - ans)

        print("Всего вызовов функций: " + str(Integral.ncalls))
        print(f"Ответ: {ans}")
        print()
        return ans

    def simpson(func, x0, x1, rtol=1.0e-10, nseg0=1):
        old_trapez_sum = Integral.restart(func, x0, x1, nseg0)
        new_trapez_sum = Integral.double_nseg(func, x0, x1)
        ans = (4 * new_trapez_sum - old_trapez_sum) / 3
        old_ans = 0.0
        err_est = max(1, abs(ans))
        while err_est > abs(rtol * ans):
            old_ans = ans
            old_trapez_sum = new_trapez_sum
            new_trapez_sum = Integral.double_nseg(func, x0, x1)
            ans = (4 * new_trapez_sum - old_trapez_sum) / 3
            err_est = abs(old_ans - ans)

        print("Всего вызовов функций: " + str(Integral.ncalls))
        print(f"Ответ: {ans}")
        print()
        return ans


def main():
    print("Выберите интеграл:")
    print("1) 2x^3 - 5x^2 - 3x + 21, 0, 2")
    print("2) 4x^3 - 3x^2 + 5x - 20, 2, 4")
    print("3) 2x^3 - 3x^2 + 4x - 22, 3, 5")

    choose = int(input("$"))
    while (choose != 1) and (choose != 2) and (choose != 3):
        choose = int(input("$"))

    if choose == 1:
        print("Метод Трапеций")
        Integral.trapezoid(lambda x: 2 * x ** 3 - 5 * x ** 2 - 3 * x + 21, 0, 2, rtol=0.01)
        print("Метод Симпсона")
        Integral.simpson(lambda x: 2 * x ** 3 - 5 * x ** 2 - 3 * x + 21, 0, 2, rtol=0.01)
        
    elif choose == 2:
        print("Метод Трапеций")
        Integral.trapezoid(lambda x: 4 * x**3 - 3 * x**2 + 5 * x - 20, 2, 4, rtol=0.01)
        print("Метод Симпсона")
        Integral.simpson(lambda x: 4 * x**3 - 3 * x**2 + 5 * x - 20, 2, 4, rtol=0.01)
        
    elif choose == 3:
        print("Метод Трапеций")
        Integral.trapezoid(lambda x: 2 * x**3 - 3 * x**2 + 4 * x - 22, 3, 8, rtol=0.01)
        print("Метод Симпсона")
        Integral.simpson(lambda x: 2 * x**3 - 3 * x**2 + 4 * x - 22, 3, 8, rtol=0.01)


if __name__ == "__main__":
    main()
