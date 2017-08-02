# coding: utf-8
import re
import sys
sys.setrecursionlimit(10 ** 6)

def read_num():
    while True:
        input_num = input()
        if re.match(r"^.*[/D].*$", input_num):
            print("Please input only num.")
            continue
        else:
            input_num = int(input_num)
            break

    return input_num


def calc_f(num):
    if num < 1:
        return 1
    else:
        return (161 * calc_f(num - 1) + 2457) % (2 ** 24)


def question_1():
    num = read_num()
    print(calc_f(num))


if __name__ == "__main__":
    question_1()
