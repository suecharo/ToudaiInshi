# coding: utf-8
import re


def read_line():
    while True:
        ret = input()
        if re.match(r"^.*([^a-z|&|\+]).*$", ret):
            print("Please input only a-z or & or +")
            continue
        else:
            break

    return ret


def question_1():
    read = read_line()
    l_read = read.split("+")
    _ = [print(i) for i in l_read]


if __name__ == "__main__":
    question_1()
