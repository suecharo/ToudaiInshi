# coding: utf-8
from collections import defaultdict

def read_file(file_name):
    f = open(file_name, "r")
    read = f.read()
    f.close()
    l_input = []
    for line in read.split("\n"):
        if line == "":
            continue
        line = list(map(int, line.split(" ")))
        l_input.append(line)
    return l_input


def write_rectangle_to_board(rect, rect_num, l_board):
    for x in range(rect[0], rect[0] + rect[2]):
        for y in range(rect[1], rect[1] + rect[3]):
            l_board[y][x].add(2)
            # l_board[y][x].append(rect_num)
    return l_board


def find_max_min_xy(l_input):
    min_x, min_y = 1000, 1000
    max_x, max_y = -1, -1
    for line in l_input:
        min_x = min(min_x, line[0])
        min_y = min(min_y, line[1])
        max_x = max(max_x, line[0] + line[2] - 1)
        max_y = max(max_y, line[1] + line[3] - 1)
    return min_x, min_y, max_x, max_y


def question_1():
    l_input = read_file("./data/7.txt")
    min_x, min_y, max_x, max_y = find_max_min_xy(l_input)
    print(min_x, min_y, max_x, max_y)
    l_board = [[set()] * (max_x + 1) for __ in range(max_y + 1)] # [y][x]
    l_board = write_rectangle_to_board([0, 0, 3, 3], 2, l_board)
    # for ind, line in enumerate(l_input):
    #     l_board = write_rectangle_to_board(line, ind, l_board)
    for line in l_board:
        print(line)
    # for line in l_input:
    #     print(line)



if __name__ == "__main__":
    question_1()
