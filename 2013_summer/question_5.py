# coding: utf-8
from collections import defaultdict
from question_3 import parse_read


def do_exe_extend(now_line_num, l_operater, d_val, sub_cache):
    ope_0, ope_1, ope_2 = l_operater
    if ope_0 == "ADD":
        if type(ope_1) is int:
            pass
        else:
            ope_1 = d_val[ope_1]
        d_val[ope_2] = ope_1

    elif ope_0 == "CMP":
        if type(ope_1) is int:
            pass
        else:
            ope_1 = d_val[ope_1]
        if type(ope_2) is int:
            pass
        else:
            ope_1 = d_val[ope_2]
        if ope_1 == ope_2:
            next_line_num = now_line_num + 2
        else:
            next_line_num = now_line_num + 1

    elif ope_0 == "JMP":
        if type(ope_1) is int:
            pass
        else:
            ope_1 = d_val[ope_1]
        next_line_num = now_line_num + ope_1

    elif ope_0 == "PRN":
        if type(ope_1) is int:
            pass
        else:
            ope_1 = d_val[ope_1]
        if type(ope_2) is int:
            pass
        else:
            ope_1 = d_val[ope_2]
        print("ope_1 : {}\nope_2 : {}".format(ope_1, ope_2))

    elif ope_0 == "SET":
        if type(ope_2) is int:
            pass
        else:
            ope_1 = d_val[ope_2]
        d_val[ope_1] = ope_2
        next_line_num = now_line_num + 1

    elif ope_0 == "SUB":
        if type(ope_1) is int:
            pass
        else:
            ope_1 = d_val[ope_1]
        next_line_num = now_line_num + ope_1
        sub_cache = now_line_num

    elif ope_0 == "BAK":
        next_line_num = sub_cache
        sub_cache = -1

    return next_line_num, d_val, sub_cache


def question_5():
    f = open("prog4.txt", "r")
    read = f.read()
    f.close()

    d_line = parse_read(read)
    d_val = defaultdict(int)
    now_line = 0
    sub_cache = -1
    while len(d_line) > now_line >= 0:
        l_operater = d_line[now_line]
        next_line, d_val, sub_cache = do_exe(now_line, l_operater, d_val, sub_cache)
        now_line = next_line


if __name__ == "__main__":
    question_5()
