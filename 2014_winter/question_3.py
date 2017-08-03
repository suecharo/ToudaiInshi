# coding: utf-8
import re

def read_num():
    while True:
        read_num = input()
        if len(read_num) != 32 or re.match(r"^.*(/D).*$", read_num):
            print("Please input only 32 disits num.")
        else:
            read_num = int(read_num)
            break
    return read_num


def question_3():
    print("Please input num_1.")
    num_1 = read_num()
    print("Please input num_2.")
    num_2 = read_num()
    print("-" * 40)
    ans = num_1 + num_2
    print("ans : {}".format(ans))


if __name__ == "__main__":
    question_3()
