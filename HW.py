import numpy as np
import matplotlib.pyplot as plt

# Коэффициенты перед х
a, b, c, d, e = -12, -18, 5, 10, -30
limit = 10
step = 0.01  # шаг вычисления
step_acr = 0.0001  # шаг вычисления с повыш точностью
line_style = '-'  # тип линии
color = 'b'  # цвет графика
direct_up = True  # флаг направления графика (возрастает/убывает)


def f(x):
    return a * x ** 4 * np.sin(np.cos(x)) + b * x ** 3 + c * x ** 2 + d * x + e


# смена типа линии графика
def switch_line():
    global line_style
    if line_style == '-':
        line_style = '-.'
    else:
        line_style = '-'
    return line_style


def switch_color():
    global color
    if color == 'g':
        color = 'r'
    else:
        color = 'g'
    return color


x = np.arange(-limit, limit + step, step)  # limit + step для предотвращения разрывов графика при построении
# первый элемент списка - граница от которой строим график
x_change = [(-limit, 'limit')]

for i in range(len(x) - 1):
    # если f(x) пересекает 0
    if f(x[i]) > 0 and f(x[i +1]) < 0 or f(x[i]) < 0 and f(x[i + 1]) > 0:
        x_acr = np.arange(x[i], x[i + 1] + step_acr, step_acr)
        for j in range(len(x_acr) - 1):
            if f(x_acr[j]) > 0 and f(x_acr[j + 1]) < 0 or f(x_acr[j]) < 0 and f(x_acr[j + 1]) > 0:
                x_change.append((x_acr[j], 'zero'))
    # если f(x) меняет направление
    if direct_up:
        if f(x[i]) > f(x[i + 1]):
            direct_up = False
            x_change.append((x[i], 'dir'))
    else:
        if f(x[i]) < f(x[i + 1]):
            direct_up = True
            x_change.append((x[i], 'dir'))

# последний элемент списка - граница от которой строим график
x_change.append((limit, 'limit'))
# print(x_change)

# построение графика
for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i + 1][0] + step, step)
    if x_change[i][1] == 'zero':
        plt.plot(x_change[i][0], f(x_change[i][0]), 'bx')
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, f(cur_x), color)
    else:
        plt.plot(cur_x, f(cur_x), switch_color())

plt.grid()
plt.show()
