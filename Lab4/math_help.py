from math import sqrt


def solve_minor(matrix, i, j):
    """ Найти минор элемента матрицы """
    n = len(matrix)
    return [[matrix[row][col] for col in range(n) if col != j] for row in range(n) if row != i]


def solve_det(matrix):
    """ Найти определитель матрицы """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    det = 0
    sgn = 1
    for j in range(n):
        det += sgn * matrix[0][j] * solve_det(solve_minor(matrix, 0, j))
        sgn *= -1
    return det


def calc_s(dots, f):
    """ Найти меру отклонения """
    n = len(dots)
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]

    return sum([(f(x[i]) - y[i]) ** 2 for i in range(n)])


def calc_stdev(dots, f):
    """ Найти среднеквадратичное отклонение """
    n = len(dots)

    return sqrt(calc_s(dots, f) / n)
