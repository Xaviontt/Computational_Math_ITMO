FILE_IN = "matrix.txt"

from Anecdote_getter.anecdote_getter import *

import psutil
import numpy as np
import sys


def read_n_console():
    n = int(input('Enter number of unknowns: '))
    return n


def read_matrix_console(n):
    matrix = np.zeros((n, n + 1))

    print('Enter Augmented Matrix Coefficients:')
    for i in range(n):
        for j in range(n + 1):
            matrix[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

    return matrix


def read_n_file():
    with open(FILE_IN, 'rt') as fin:
        n = int(fin.readline())

    return n


def read_matrix_file():
    with open(FILE_IN, 'rt') as fin:
        try:
            n = int(fin.readline())
            matrix = []
            for line in fin:
                new_row = list(map(float, line.strip().split()))
                if len(new_row) != (n + 1):
                    raise ValueError
                matrix.append(new_row)
            if len(matrix) != n:
                raise ValueError
        except ValueError:
            return
    return matrix


def print_matrix(matrix):
    print(matrix)
    return


def straight_stroke(n, matrix):
    for i in range(n):
        if matrix[i][i] == 0.0:
            sys.exit('Divide by zero detected!')

        for j in range(i + 1, n):
            ratio = matrix[j][i] / matrix[i][i]

            for k in range(n + 1):
                matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    return matrix


# Обратный ход
def reverse_stroke(n, matrix):
    x = np.zeros(n)

    x[n - 1] = matrix[n - 1][n] / matrix[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = matrix[i][n]

        for j in range(i + 1, n):
            x[i] = x[i] - matrix[i][j] * x[j]

        x[i] = x[i] / matrix[i][i]

    return x


def main():
    get_anecdote()

    print("\nHow do you want to enter the coefficients?")
    print("1 - enter from the keyboard")
    print("2 - take from file\n")

    method = input("$")
    while (method != '1') and (method != '2'):
        print("Enter '1' or '2' to select input method.")
        method = input("$")

    if method == '1':
        n = read_n_console()
        matrix = read_matrix_console(n)
    else:
        n = read_n_file()
        matrix = read_matrix_file()

    if matrix is None:
        print("Error, please check your input and try again")
        return

    triangular_matrix = straight_stroke(n, matrix)

    print("\nTriangular matrix: ")
    for row in triangular_matrix:
        for col in row:
            print('{:10}'.format(round(col, 2)), end='')
        print()

    answer = reverse_stroke(n, triangular_matrix)

    print('\nRequired solution is: ')
    for i in range(n):
        print('X%d = %0.2f' % (i, answer[i]), end='\n')


if __name__ == "__main__":
    main()
