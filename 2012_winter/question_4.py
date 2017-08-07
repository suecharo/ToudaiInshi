# coding: utf-8
from question_2 import read_point
from question_2 import make_matrix
from question_2 import draw_point
from question_2 import change_matrix_to_str
from question_3 import make_point_from_line

def approximate_from_point(read_point):
    sum_xy = 0
    sum_x_2 = 0
    sum_x = 0
    sum_y = 0
    for (x, y) in read_point:
        sum_x += x
        sum_y += y
        sum_xy += x * y
        sum_x_2 += x ** 2

    a_top = (len(read_point) * sum_xy - sum_x * sum_y)
    ab_under = (len(read_point) * sum_x_2 - sum_x ** 2)
    b_top = (sum_x_2 * sum_y - sum_xy * sum_x)
    if ab_under == 0:
        ab_under = 0.00000000001

    a = a_top / ab_under
    b = b_top / ab_under

    return a, b


def question_4():
    l_read = read_point("data1.txt")
    matrix = make_matrix()
    a, b = approximate_from_point(l_read)
    l_point = make_point_from_line(a, b)
    matrix = draw_point(l_read, matrix, "*")
    matrix = draw_point(l_point, matrix, "o")
    str_matrix = change_matrix_to_str(matrix)
    print(str_matrix)


if __name__ == "__main__":
    question_4()
