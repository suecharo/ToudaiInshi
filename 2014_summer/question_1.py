# coding: utf-8
import re

def read_float():
    while True:
        read = input()
        if re.match("^.*^(/d|\.).*$", read):
            print("Please input only float")
            continue
        else:
            try:
                read = float(read)
            except:
                print("Please input only float")
                continue
            break

    return read


def question_1():
    num = read_float()
    print(num)
    p_q = 0
    while num * p_q <= 10:
        p_q += 1
    else:
        p_q -= 1

    print((p_q + 1) * (p_q + 1))


if __name__ == "__main__":
    question_1()
