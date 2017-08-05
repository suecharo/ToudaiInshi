# coding: utf-8
from collections import defaultdict
from question_3 import parse_read
import copy


def do_exe_extend_2(now_line_num, l_operater, d_val, sub_cache, all_operater):
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

    elif ope_0 == "CAL":
        if type(ope_1) is int:
            pass
        else:
            ope_1 = d_val[ope_1]
        if type(ope_2) is int:
            pass
        else:
            ope_2 = d_val[ope_2]

        sub_cache = now_line_num
        sub_val = copy.copy(d_val)
        sub_val["in"] = ope_2
        sub_line_num = now_line_num + ope_1
        while True:
            sub_line_num, sub_val, sub_cache = do_exe_extend_2(sub_line_num, all_operater[sub_line_num], sub_val, sub_cache, all_operater)
            if sub_line_num == -1:
                d_val["out"]

    elif ope_0 == "RET":
        next_line_num = -1

    return next_line_num, d_val, sub_cache


        if type(ope_1) is int:
            pass
        else:
            ope_1 = d_val[ope_1]
        if type(ope_2) is int:
            pass
        else:
            ope_2 = d_val[ope_2]







def question_6():
    f = open("prog5.txt", "r")
    read = f.read()
    f.close()

    d_line = parse_read(read)
    d_val = defaultdict(int)
    now_line = 0
    sub_cache = -1
    while len(d_line) > now_line >= 0:
        l_operater = d_line[now_line]
        now_line, d_val, sub_cache = do_exe(now_line, l_operater, d_val, sub_cache)


if __name__ == "__main__":
    question_6()
