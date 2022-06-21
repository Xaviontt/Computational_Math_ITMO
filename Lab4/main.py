from approximation import *
from plot import *
from input import *

FILE_IN = "input.txt"
FILE_OUT = "output.txt"


def main():

    data = getdata_file()

    answers = []
    temp_answers = [lin_func(data['dots']),
                    sqrt_func(data['dots']),
                    exp_func(data['dots']),
                    log_func(data['dots']),
                    pow_func(data['dots']),
                    x3_func(data['dots'])
                    ]

    for answer in temp_answers:
        if answer is not None:
            answers.append(answer)

    # print("\n\n%30s%30s%30s" % ("Вид функции", "Мера отклонения ", "Ср. отклонение"))
    # print("-" * 60)
    # for answer in answers:
    #     print("%30s%30s%30.4f" % (answer['str_f'], round(answer['s'], 4), answer['stdev']))

    print("\n%30s%20s" % ("Вид функции", "Ср. отклонение"))
    for answer in answers:
        print("%30s%20.4f" % (answer['str_f'],  answer['stdev']))

    x = np.array([dot[0] for dot in data['dots']])
    y = np.array([dot[1] for dot in data['dots']])
    plot_x = np.linspace(np.min(x), np.max(x), 100)
    plot_y = []
    labels = []

    for answer in answers:
        plot_y.append([answer['f'](x) for x in plot_x])
        labels.append(answer['str_f'])

    plot(x, y, plot_x, plot_y, labels)
    best_answer = min(answers, key=lambda z: z['stdev'])
    # best_answer = answers[]
    print("\nЛучшая функция.")
    print(f" {best_answer['str_f']}, где")
    print(f"  a = {round(best_answer['a'], 4)}")
    print(f"  b = {round(best_answer['b'], 4)}")
    print(f"  c = {round(best_answer['c'], 4) if 'c' in best_answer else '-'}")
    print(f"  d = {round(best_answer['d'], 4) if 'd' in best_answer else '-'}")

    pirs_coef = np.corrcoef(x, y)[0, 1]
    print(f"\nКоэффициент Пирсона: {pirs_coef}")


if __name__ == "__main__":
    main()
