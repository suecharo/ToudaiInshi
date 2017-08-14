# coding: utf-8
from question_2_1 import read_file, make_d_edges, find_joined_graph


def calc_cluster_num(d_edges, ver_num):
    next_ver = d_edges[ver_num]
    if len(next_ver) - 1 <= 0:
        return 0
    s_next_ver = set(next_ver)
    edge_count = 0
    for n_ver in next_ver:
        next_next_ver = d_edges[n_ver]
        for n_n_ver in next_next_ver:
            if n_n_ver in s_next_ver:
                edge_count += 1
            else:
                continue
    ret_ans = edge_count / (len(next_ver) * (len(next_ver) - 1))
    return ret_ans


def question_2_2():
    l_read = read_file()
    d_edges = make_d_edges(l_read, 181)
    for i in range(1, 11):
        ret_ans = calc_cluster_num(d_edges, i)
        print("{} : {}".format(i, ret_ans))


if __name__ == "__main__":
    question_2_2()
