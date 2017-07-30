# coding: utf-8
from question_2 import change_row_to_col


def change_char_list_to_5(char_list):
    len_col = len(char_list[0])
    out_bool = False
    for i in range(len_col):
        for j in range(4):
            a_char = char_list[j][i]
            if a_char != " ":
                pos = i
                out_bool = True
                break
        if out_bool:
            break

    ret_list = []
    for col in char_list:
        short_col = col[i:i+5]
        ret_list.append(short_col)

    return ret_list


def check_char_rows(char_rows):
    row_2 = char_rows[1]
    row_4 = char_rows[3]

    if row_2 == "|  |" and row_4 == "|  |": # 0, 8
        row_3 = char_rows[2]
        if row_3[1] == "*" or row_3[2] == "*":
            return "8"
        else:
            return "0"
    elif row_2 == "|  |" and row_4 == "   |": # 4, 9
        row_1 = char_rows[0]
        if row_1[1] == "*" or row_1[2] == "*":
            return "9"
        else:
            return "4"
    elif row_2 == "|  |" and row_4 == "|   ": # nothing, maybe 0 or 8
        row_3 = char_rows[2]
        if row_3[1] == "*" or row_3[2] == "*":
            return "8"
        else:
            return "0"
    elif row_2 == "|   " and row_4 == "|  |": # 6
        return "6"
    elif row_2 == "|   " and row_4 == "   |": # nothing, maybe 4, 6, 9
        row_1 = char_rows[0]
        row_5 = char_rows[4]
        if row_1[1] == "*" or row_3[2] == "*":
            return "9"
        elif row_5[1] == "*" or row_5[2] == "*":
            return "6"
        else:
            return "4"
    elif row_2 == "|   " and row_4 == "|   ": # 5
        return "5"
    elif row_2 == "   |" and row_4 == "|  |": # nothing, maybe 0 or 8
        row_3 = char_rows[2]
        if row_3[1] == "*" or row_3[2] == "*":
            return "8"
        else:
            return "0"
    elif row_2 == "   |" and row_4 == "   |": # 3, 7
        row_3 = char_rows[2]
        if row_3[0] == "*" or row_3[1] == "*":
            return "3"
        else:
            return "7"
    elif row_2 == "|  |" and row_4 == "|   ": # nothing, maybe 0 or 8
        row_3 = char_rows[2]
        if row_3[1] == "*" or row_3[2] == "*":
            return "8"
        else:
            return "0"
    else:
        if row_2 == "|  |": # 4, 9
            row_1 = char_rows[0]
            if row_1[1] == "*" or row_1[2] == "*":
                return "9"
            else:
                return "4"
        elif row_4 == "|  |": # 6
            return "6"
        else: # 7
            return "7"


def change_cols_to_rows(col_list):
    ret_rows = []
    for i in range(5):
        row = ""
        for j in range(4):
            row += col_list[j][i]
        ret_rows.append(row)
    return ret_rows


def question_5():
    f = open("out5.txt", "r")
    read_text = f.read()
    f.close

    read_lines = read_text.split("\n")
    max_len_row = max([len(row) for row in read_lines])
    max_len_col = len(read_lines)
    for i in range(max_len_col):
        row = read_lines[i]
        if len(row) == max_len_row:
            continue
        else:
            dif = max_len_row - len(row)
            read_lines[i] += " " * dif

    col_all_brank = " " * max_len_col

    char_nums = []
    l_col = change_row_to_col(read_lines)

    col_ind = 0
    now_char = []
    while col_ind <= max_len_row - 1:
        now_col = l_col[col_ind]
        if now_col == col_all_brank:
            if len(now_char) != 0:
                char_nums.append(now_char)
                now_char = []
            col_ind += 1
            continue

        now_char.append(now_col)
        col_ind += 1
    else:
        if len(now_char) != 0:
            char_nums.append(now_char)

    print_nums = []
    for char in char_nums:
        if len(char) <= 2:
            print_nums.append("1")
        else:
            char_cols = change_char_list_to_5(char)
            char_rows = change_cols_to_rows(char_cols)
            num = check_char_rows(char_rows)
            print_nums.append(num)

    print_text = "".join(print_nums)
    print(print_text)


if __name__ == "__main__":
    question_5()
