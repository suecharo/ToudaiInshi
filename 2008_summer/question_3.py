# coding: utf-8
from question_2_1 import read_file, make_d_edges, find_joined_graph
from question_2_3 import calc_ave_cluster_num
from collections import defaultdict
from itertools import combinations


def calc_distance_all(d_edges, joined_graph):
    INF = 10 ** 20
    d_dis = defaultdict(lambda : defaultdict(int))
    for ver_fro in joined_graph:
        for ver_to in joined_graph:
            if ver_fro == ver_to:
                d_dis[ver_fro][ver_to] = 0
            else:
                if ver_to in d_edges[ver_fro]:
                    d_dis[ver_fro][ver_to] = 1
                else:
                    d_dis[ver_fro][ver_to] = INF
    for k_ver in joined_graph:
        for i_ver in joined_graph:
            for j_ver in joined_graph:
                d_dis[i_ver][j_ver] = min(d_dis[i_ver][j_ver], d_dis[i_ver][k_ver] + d_dis[k_ver][j_ver])
    return d_dis


# def calc_distance_fro_to(d_edges, graph, fro, to):
#     if fro == to:
#         return 0
#     for ind, sub_graph in enumerate(graph):
#         if fro in sub_graph:
#             fro_ind = ind
#         if to in sub_graph:
#             to_ind = ind
#     if fro_ind != to_ind:
#         return "INF"
#     else:
#         d_dis = calc_distance_all(d_edges, graph[fro_ind])
#         return d_dis[fro][to]


def calc_ave_diameter(d_dis):
    dia_sum = 0
    for i, j in combinations(list(range(1, 101)), 2):
        dia_sum += d_dis[i][j]
    ans = dia_sum / (99 * 50)
    return ans


def question_3():
    l_read = read_file()
    d_edges_graph_3 = make_d_edges(l_read, 202)
    d_edges_graph_4 = make_d_edges(l_read, 302)
    graph_3 = set(range(1, 101))
    graph_4 = set(range(1, 101))
    # graph_3, graph_4 共に前提条件より連結
    dis_3 = calc_distance_all(d_edges_graph_3, graph_3)
    dis_4 = calc_distance_all(d_edges_graph_4, graph_4)
    print("dis_3 27 -> 63 : {}".format(dis_3[27][63]))
    print("dis_4 27 -> 63 : {}".format(dis_4[27][63]))
    ave_dia_3 = calc_ave_diameter(dis_3)
    ave_dia_4 = calc_ave_diameter(dis_4)
    print("average_dia_3 : {}".format(ave_dia_3))
    print("average_dia_4 : {}".format(ave_dia_4))


if __name__ == "__main__":
    question_3()
