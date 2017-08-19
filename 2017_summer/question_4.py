# coding: utf-8
from question_2 import read_file
from question_2 import change_row_to_col


def change_l_col_to_num_expand(l_col):
    print_num = ""
    col_ind = 0
    col_all_brank = " " * len(l_col[0])
    while col_ind <= len(l_col) - 1:
        now_col = l_col[col_ind]
        if now_col == col_all_brank:
            col_ind += 1
            continue

        row_ind = 0
        for ind, char in enumerate(now_col):
            if char != " ":
                row_ind = ind
                break
        now_col = now_col[row_ind:row_ind + 5]

        if now_col == "*|*|*": # 0, 1, 6, 8
            if col_ind == len(l_col) - 1:
                print_num += "1"
                break
            next_col = l_col[col_ind + 1][row_ind:row_ind + 5]
            if next_col == "*   *": # 0
                print_num += "0"
                col_ind += 5
            elif next_col == "     ": # 1
                print_num += "1"
                col_ind += 2
            elif next_col == "  * *": # 6
                print_num += "6"
                col_ind += 5
            elif next_col == "* * *": # 8
                print_num += "8"
                col_ind += 5

        elif now_col == "* *|*": # 2,
            print_num += "2"
            col_ind += 5
        elif now_col == "* * *": # 3
            print_num += "3"
            col_ind += 5
        elif now_col == "*|*  ": # 4, 9
            next_col = l_col[col_ind + 1][row_ind:row_ind + 5]
            if next_col == "  *  ": # 4
                print_num += "4"
                col_ind += 5
            elif next_col == "* *  ": # 9
                print_num += "9"
                col_ind += 5
        elif now_col == "*|* *": # 5
            print_num += "5"
            col_ind += 5
        elif now_col == "*    ": # 7
            print_num += "7"
            col_ind += 5

    return print_num


def question_4():
    read_text = read_file("out3.txt")
    read_lines = read_text.split("\n")
    l_col = change_row_to_col(read_lines)
    print_num = change_l_col_to_num_expand(l_col)
    print(print_num)


if __name__ == "__main__":
    question_4()
