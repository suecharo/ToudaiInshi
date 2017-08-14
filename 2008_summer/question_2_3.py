# coding: utf-8
from question_2_1 import read_file, make_d_edges, find_joined_graph
from question_2_2 import calc_cluster_num


def calc_ave_cluster_num(d_edges):
    sum_cluster_num = 0
    for i in range(1, 101):
        ret = calc_cluster_num(d_edges, i)
        sum_cluster_num += ret
    ret_ans = sum_cluster_num /100
    return ret_ans


def question_2_3():
    l_read = read_file()
    d_edges = make_d_edges(l_read, 181)
    ret_ans = calc_ave_cluster_num(d_edges)
    print(ret_ans)


if __name__ == "__main__":
    question_2_3()
