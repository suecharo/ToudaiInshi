# coding: utf-8
import re

def read(file_name):
    f = open(file_name, "r")
    read_file = f.read()
    f.close()
    return read_file


def count_num(l_lines):
    count = 0
    for line in l_lines:
        for ele in line:
            if re.match(r"[0-9]", ele):
                count += 1
    count //= 3
    return count


def question_2():
    c_1 = read("./data/c1.txt")
    c_2 = read("./data/c2.txt")
    ans_c_1 = count_num(c_1)
    ans_c_2 = count_num(c_2)
    print("c1.txt : {}".format(ans_c_1))
    print("c2.txt : {}".format(ans_c_2))


if __name__ == "__main__":
    question_2()
