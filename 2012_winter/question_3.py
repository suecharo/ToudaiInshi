# coding: utf-8
from question_2 import make_matrix
from question_2 import draw_point
from question_2 import change_matrix_to_str
import math

def make_point_from_line(a, b, num_point=20):
    # x = 0
    y_0 = b
    # x = 30
    y_30 = a * 30 + b
    # y = 0
    x_0 = - (b / a)
    # y = 29
    x_30 = (30 - b) / a

    x_from_to = []
    for ind, ele in enumerate([y_0, y_30, x_0, x_30]):
        if 0 <= ele <= 30:
            if ind == 0:
                x_from_to.append(0)
            elif ind == 1:
                x_from_to.append(30)
            elif ind == 2:
                x_from_to.append(ele)
            elif ind == 3:
                x_from_to.append(ele)
    x_from_to.sort()
    x_from, x_to = x_from_to[0], x_from_to[-1]
    dif_x = (x_to - x_from) / (num_point - 1)

    l_point = []
    for i in range(num_point):
        x = x_from + dif_x * i
        y = a * x + b

        x_floor = math.floor(x)
        if x - x_floor >= 0.5:
            x = x_floor + 0.5
        else:
            x = x_floor
        y = math.floor(y)

        l_point.append([x, y])

    return l_point


def question_3():
    matrix = make_matrix()
    l_point = make_point_from_line(0.8, 2)
    matrix = draw_point(l_point, matrix, "o")
    str_matrix = change_matrix_to_str(matrix)
    print(str_matrix)


if __name__ == "__main__":
    question_3()
