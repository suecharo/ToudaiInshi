# coding: utf-8
from collections import defaultdict

def parse_read(read_file):
    d_line = dict()
    l_read = read_file.split("\n")
    for ind, line in enumerate(l_read):
        l_line = line.split(" ")
        for i in [1, 2]:
            ope = l_line[i]
            try:
                ope = int(ope)
                l_line[i] = ope
            except:
                pass

        d_line[ind] = l_line

    return d_line


def do_exe(now_line_num, l_operater, d_val):
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

    return next_line_num, d_val


def question_3():
    f = open("prog1.txt", "r")
    read = f.read()
    f.close()

    d_line = parse_read(read)
    d_val = defaultdict(int)
    now_line = 0
    while len(d_line) > now_line >= 0:
        l_operater = d_line[now_line]
        next_line, d_val = do_exe(now_line, l_operater, d_val)
        now_line = next_line


if __name__ == "__main__":
    question_3()
