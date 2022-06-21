import matplotlib.pyplot as plt


def plot(x, y, plot_x, plot_y):
    """ Отрисовать график по заданным координатам узлов и точкам многочлена """
    # Настраиваем всплывающее окно
    # plt.rcParams['toolbar'] = 'None'
    # Настриваем оси
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.plot(1, 0, marker=">", ms=5, color='k',
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, marker="^", ms=5, color='k',
            transform=ax.get_xaxis_transform(), clip_on=False)

    # Отрисовываем график
    plt.plot(x, y, 'o', plot_x, plot_y)
    plt.show(block=False)

