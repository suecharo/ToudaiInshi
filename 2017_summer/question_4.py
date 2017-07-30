# coding: utf-8
from question_2 import change_row_to_col

def long_col_to_5(col):
    for i in range(len(col)):
        if col[i] != " ":
            ret_col = "".join(col[i:i + 5])
            break
    return ret_col


def find_pos(col):
    for i in range(len(col)):
        if col[i] != " ":
            return i


def long_col_to_5_next(col, ind):
    ret_col = "".join(col[ind:ind + 5])
    return ret_col


def question_4():
    f = open("out3.txt", "r")
    read_text = f.read()
    f.close

    print_num = []
    read_lines = read_text.split("\n")
    len_col = len(read_lines)
    col_all_brank = " " * len_col
    l_col = change_row_to_col(read_lines)

    col_ind = 0
    while col_ind <= len(l_col) - 1:
        now_col = l_col[col_ind]
        if now_col == col_all_brank:
            col_ind += 1
            continue

        changed_now_col = long_col_to_5(now_col)
        if changed_now_col == "*|*|*": # 0, 1, 6, 8
            if col_ind == len(l_col) - 1:
                print_num.append("1")
                break
            else:
                next_col = l_col[col_ind + 1]
                if next_col == col_all_brank: # 1
                    print_num.append("1")
                    col_ind += 1
                else:
                    now_pos = find_pos(now_col)
                    next_col = long_col_to_5_next(next_col, now_pos)
                    if next_col == "*   *": # 0
                        print_num.append("0")
                        col_ind += 4
                    elif next_col == "  * *": # 6
                        print_num.append("6")
                        col_ind += 4
                    elif next_col == "* * *": # 8
                        print_num.append("8")
                        col_ind += 4
        elif changed_now_col == "* *|*": # 2,
            print_num.append("2")
            col_ind += 4
        elif changed_now_col == "* * *": # 3
            print_num.append("3")
            col_ind += 4
        elif changed_now_col == "*|*  ": # 4, 9
            next_col = l_col[col_ind + 1]
            now_pos = find_pos(now_col)
            next_col = long_col_to_5_next(next_col, now_pos)
            if next_col == "  *  ": # 4
                print_num.append("4")
                col_ind += 4
            elif next_col == "* *  ": # 9
                print_num.append("9")
                col_ind += 4
        elif changed_now_col == "*|* *": # 5
            print_num.append("5")
            col_ind += 4
        elif changed_now_col == "*    ": # 7
            print_num.append("7")
            col_ind += 4

    print_text = "".join(print_num)
    print(print_text)


if __name__ == "__main__":
    question_4()
