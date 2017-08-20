# coding: utf-8
import re
import sys
sys.setrecursionlimit(10 ** 6)

def read_num():
    input_num = input()
    if re.search(r"\D", input_num):
        print("Please input only num.")
        return read_num()
    return input_num


def calc_f(num):
    if num < 1:
        return 1
    else:
        return (161 * calc_f(num - 1) + 2457) % (2 ** 24)


def question_1():
    num = int(read_num())
    print(calc_f(num))


if __name__ == "__main__":
    question_1()
