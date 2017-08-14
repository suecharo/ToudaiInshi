# coding: utf-8
from question_2_1 import read_file, make_d_edges
from question_2_3 import calc_ave_cluster_num


def question_2_5():
    l_read = read_file()
    d_edges_202 = make_d_edges(l_read, 202)
    d_edges_302 = make_d_edges(l_read, 302)
    clu_num_202 = calc_ave_cluster_num(d_edges_202)
    clu_num_302 = calc_ave_cluster_num(d_edges_302)
    print("202 : {}".format(clu_num_202))
    print("302 : {}".format(clu_num_302))


if __name__ == "__main__":
    question_2_5()
