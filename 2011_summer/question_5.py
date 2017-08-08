# coding: utf-8
from question_2 import read
from question_2 import count_num
import re


def unzip(read_file):
    ret_str = ""
    str_ind = 0
    while str_ind != len(read_file):
        char = read_file[str_ind]
        if re.match(r"[0-9]", char):
            num = int(read_file[str_ind:str_ind + 3])
            str_ind += 3
            for i in range(6):
                ret_str += ret_str[num + i]
        else:
            ret_str += char
            str_ind += 1

    return ret_str


def question_5():
    c_1 = read("./data/c1.txt")
    c_2 = read("./data/c2.txt")
    str_unzip_1 = unzip(c_1)
    str_unzip_2 = unzip(c_2)
    print("c1.txt : len - {}, tail - {}".format(len(str_unzip_1), str_unzip_1[len(str_unzip_1) - 10:]))
    print("c2.txt : len - {}, tail - {}".format(len(str_unzip_2), str_unzip_2[len(str_unzip_2) - 10:]))


if __name__ == "__main__":
    question_5()
