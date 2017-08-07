# coding: utf-8
def read_point(data):
    f = open(data, "r")
    read = f.read()
    f.close()
    l_read = []
    for line in read.split("\n"):
        line = line[1:-1]
        x, y = map(int, line.split(","))
        l_read.append([x, y])

    return l_read


def make_matrix():
    matrix = [[" "] * 64 for __ in range(32)] # [y][x]
    for ind_y in range(32):
        for ind_x in range(64):
            if ind_y == 0:
                if ind_x == 0:
                    matrix[ind_y][ind_x] = "3"
                elif ind_x == 1:
                    matrix[ind_y][ind_x] = "0"
                elif ind_x == 2:
                    matrix[ind_y][ind_x] = "|"
            elif ind_y == 10:
                if ind_x == 0:
                    matrix[ind_y][ind_x] = "2"
                elif ind_x == 1:
                    matrix[ind_y][ind_x] = "0"
                elif ind_x == 2:
                    matrix[ind_y][ind_x] = "|"
            elif ind_y == 20:
                if ind_x == 0:
                    matrix[ind_y][ind_x] = "1"
                elif ind_x == 1:
                    matrix[ind_y][ind_x] = "0"
                elif ind_x == 2:
                    matrix[ind_y][ind_x] = "|"
            elif ind_y == 30:
                if ind_x == 0:
                    matrix[ind_y][ind_x] = "0"
                elif ind_x == 1:
                    matrix[ind_y][ind_x] = " "
                elif ind_x == 2:
                    matrix[ind_y][ind_x] = "+"
                else:
                    matrix[ind_y][ind_x] = "-"
            elif ind_y == 31:
                if ind_x == 2:
                    matrix[ind_y][ind_x] = "0"
                elif ind_x == 22:
                    matrix[ind_y][ind_x] = "1"
                elif ind_x == 23:
                    matrix[ind_y][ind_x] = "0"
                elif ind_x == 42:
                    matrix[ind_y][ind_x] = "2"
                elif ind_x == 43:
                    matrix[ind_y][ind_x] = "0"
                elif ind_x == 62:
                    matrix[ind_y][ind_x] = "3"
                elif ind_x == 63:
                    matrix[ind_y][ind_x] = "0"
            else:
                if ind_x == 2:
                    matrix[ind_y][ind_x] = "|"

    return matrix


def draw_point(l_point, matrix, mark):
    for (x, y) in l_point:
        point_x = int(2 * (x + 1))
        point_y = int(30 - y)
        matrix[point_y][point_x] = mark
    return matrix


def change_matrix_to_str(draw_matrix):
    ret_str = "\n".join(["".join(row) for row in draw_matrix])
    return ret_str


def question_2():
    l_read = read_point("data1.txt")
    matrix = make_matrix()
    matrix = draw_point(l_read, matrix, "*")
    str_matrix = change_matrix_to_str(matrix)
    print(str_matrix)


if __name__ == "__main__":
    question_2()
