# coding: utf-8
def read_file(text_name):
    f = open(text_name, "r")
    ret = f.read()
    f.close()
    return ret


def change_row_to_col(l_text):
    len_col = len(l_text[0])
    len_row = len(l_text)
    ret_cols = []
    for i in range(len_col):
        col = ""
        for j in range(len_row):
            col += l_text[j][i]
        ret_cols.append(col)
    return ret_cols


def change_l_col_to_num(l_col):
    print_num = ""
    col_ind = 0
    while col_ind <= len(l_col) - 1:
        now_col = l_col[col_ind]
        if now_col == "*|*|*": # 0, 1, 6, 8
            if col_ind == len(l_col) - 1:
                print_num += "1"
                break
            next_col = l_col[col_ind + 1]
            if next_col == "*   *": # 0
                print_num += "0"
                col_ind += 6
            elif next_col == "     ": # 1
                print_num += "1"
                col_ind += 3
            elif next_col == "  * *": # 6
                print_num += "6"
                col_ind += 6
            elif next_col == "* * *": # 8
                print_num += "8"
                col_ind += 6

        elif now_col == "* *|*": # 2,
            print_num += "2"
            col_ind += 6
        elif now_col == "* * *": # 3
            print_num += "3"
            col_ind += 6
        elif now_col == "*|*  ": # 4, 9
            next_col = l_col[col_ind + 1]
            if next_col == "  *  ": # 4
                print_num += "4"
                col_ind += 6
            elif next_col == "* *  ": # 9
                print_num += "9"
                col_ind += 6
        elif now_col == "*|* *": # 5
            print_num += "5"
            col_ind += 6
        elif now_col == "*    ": # 7
            print_num += "7"
            col_ind += 6

    return print_num


def question_2():
    input_file = read_file("out1.txt")
    read_lines = input_file.split("\n")
    l_col = change_row_to_col(read_lines)
    print_num = change_l_col_to_num(l_col)
    print(print_num)


if __name__ == "__main__":
    question_2()
