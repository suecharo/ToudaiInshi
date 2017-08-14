# coding: utf-8
from question_2_1 import read_file, make_d_edges
from question_3 import calc_distance_all, calc_ave_diameter


def question_4():
    l_read = read_file()
    d_edges_graph_3 = make_d_edges(l_read, 202)
    graph = set(range(1, 101))
    edge_num = 202
    while edge_num < 4950:
        edge_num += 1
        new_edge = list(map(int, l_read[edge_num - 1].split(" ")))
        d_edges_graph_3[new_edge[0]].add(new_edge[1])
        d_edges_graph_3[new_edge[1]].add(new_edge[0])
        d_dis = calc_distance_all(d_edges_graph_3, graph)
        ave_dia = calc_ave_diameter(d_dis)
        print("{} : {}".format(edge_num, ave_dia))


if __name__ == "__main__":
    question_4()
