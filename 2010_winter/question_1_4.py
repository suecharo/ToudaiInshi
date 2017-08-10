# coding: utf-8
from question_1_1 import read_file
from question_1_3 import setup_VAR
from question_1_3 import update_VAR
from collections import defaultdict
from copy import copy


def question_1_4():
    l_edges = read_file("./data/a.txt")
    pre_V, pre_A, pre_R = setup_VAR()
    d_edges = defaultdict(set)
    outer_loop = False
    for t in range(1, len(l_edges)):
        edge = l_edges[t - 1]
        d_edges, now_V, now_A, now_R = update_VAR(edge, d_edges, pre_V, pre_A, pre_R)
        if len(pre_R) != len(now_R):
            dif_R = now_R - pre_R
            for v in dif_R:
                if 0 in d_edges[v]:
                    print(t)
                    outer_loop = True
                    break
        if outer_loop:
            break
        pre_V, pre_A, pre_R = now_V, now_A, now_R


if __name__ == "__main__":
    question_1_4()
