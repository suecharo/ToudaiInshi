# coding: utf-8
from question_2 import read_point
from question_2 import make_matrix
from question_2 import draw_point
from question_2 import change_matrix_to_str
from question_3 import make_point_from_line
from question_4 import approximate_from_point

def calc_error(a, b, l_point):
    error = 0
    for (x, y) in l_point:
        error += (y - (a * x + b)) ** 2
    return error


def approximate_dowble(l_read):
    l_read.sort(key=lambda x: x[0])
    l_x_m = []
    for x_m in range(1, 31):
        for ind, point in enumerate(l_read):
            if point[0] >= x_m:
                break
        l_point_1 = l_read[:ind]
        l_point_2 = l_read[ind:]
        a_1, b_1 = approximate_from_point(l_point_1)
        a_2, b_2 = approximate_from_point(l_point_2)

        error_1 = calc_error(a_1, b_1, l_point_1)
        error_2 = calc_error(a_2, b_2, l_point_2)
        sum_error = error_1 + error_2
        l_x_m.append([sum_error, a_1, b_1, a_2, b_2, x_m])

    l_x_m.sort(key=lambda x: x[0])
    return l_x_m[0][1:]


def question_5():
    l_read = read_point("data1.txt")
    matrix = make_matrix()
    a_1, b_1, a_2, b_2, x_m = approximate_dowble(l_read)
    l_point_1 = make_point_from_line(a_1, b_1, 10)
    l_point_2 = make_point_from_line(a_2, b_2, 10)
    matrix = draw_point(l_read, matrix, "*")
    matrix = draw_point(l_point_1, matrix, "o")
    matrix = draw_point(l_point_2, matrix, "o")
    str_matrix = change_matrix_to_str(matrix)
    print(str_matrix)


if __name__ == "__main__":
    question_5()
