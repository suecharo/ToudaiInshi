# coding: utf-8
from question_1_1 import read_file
from collections import defaultdict


def question_1_2():
    l_edges = read_file("./data/a.txt")
    d_ver_in = defaultdict(int)
    d_ver_out = defaultdict(int)
    for v_x, v_y in l_edges:
        d_ver_in[v_y] += 1
        d_ver_out[v_x] += 1

    ans_in = sorted(d_ver_in.items(), key=lambda x: -x[1])[0]
    ans_out = sorted(d_ver_out.items(), key=lambda x: -x[1])[0]
    print("out -- vertex : {}, num : {}".format(ans_out[0], ans_out[1]))
    print("in -- vertex : {}, num : {}".format(ans_in[0], ans_in[1]))


if __name__ == "__main__":
    question_1_2()
