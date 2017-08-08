# coding: utf-8
from question_2 import read
from question_4 import compress
from question_5 import unzip
import re


def split_1000(read_file):
    l_ret = []
    div = len(read_file) // 1000
    for i in range(div + 1):
        if i == div:
            l_ret.append(read_file[i * 1000:])
        else:
            l_ret.append(read_file[i * 1000:(i + 1) * 1000])

    return l_ret


def compress_extend(read_file):
    ret_str = "".join(map(compress, split_1000(read_file)))
    return ret_str


def unzip_extend(read_file):
    all_ret_str = ""
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

        if len(ret_str) == 1000:
            all_ret_str += ret_str
            ret_str = ""
    else:
        all_ret_str += ret_str

    return all_ret_str


def question_6():
    s_3 = read("./data/s3.txt")
    s_3_compress_unzip = unzip_extend(compress_extend(s_3))
    if s_3 == s_3_compress_unzip:
        print("OK")
    else:
        print("NG")


if __name__ == "__main__":
    question_6()
