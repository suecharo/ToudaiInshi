# coding: utf-8
from question_1 import read_file
from collections import defaultdict

def count_char(sentense, d_count):
    for i in range(len(sentense)):
        char = sentense[i]
        c_ord = ord(char)
        if 65 <= c_ord <= 90:
            d_count[c_ord + 32] += 1
        elif 97 <= c_ord <= 122:
            d_count[c_ord] += 1

    return d_count


def question_2_1():
    read = read_file("q1.txt")
    l_read = read.split("\n")
    d_count = defaultdict(int)
    for row in l_read:
        d_count = count_char(row, d_count)
    l_count = list(d_count.items())
    l_count.sort(key=lambda x: x[0])
    for c_ord, count in l_count:
        print("{} : {}".format(chr(c_ord), count))


if __name__ == "__main__":
    question_2_1()
