# coding: utf-8
from question_2_1 import read_file, make_d_edges, find_joined_graph
from question_2_3 import calc_ave_cluster_num


def join_by_edge(joined_graph, edge):
    ver_a, ver_b = edge
    ind_a, ind_b = 0, 0
    for ind, graph in enumerate(joined_graph):
        if ver_a in graph:
            ind_a = ind
        if ver_b in graph:
            ind_b = ind
    if ind_a != ind_b:
        ind_a, ind_b = sorted([ind_a, ind_b])
        joined_graph[ind_a] = joined_graph[ind_a] | joined_graph[ind_b]
        joined_graph = joined_graph[:ind_b] + joined_graph[ind_b + 1:]
    return joined_graph


def question_2_4():
    l_read = read_file()
    d_edges_99 = make_d_edges(l_read, 99)
    joined_graph = find_joined_graph(d_edges_99)
    count = 99
    while len(joined_graph) != 1:
        count += 1
        edge = tuple(map(int, l_read[count - 1].split(" ")))
        joined_graph = join_by_edge(joined_graph, edge)
    print(count)
    print("-" * 40)
    d_edges_joined = make_d_edges(l_read, count)
    print(calc_ave_cluster_num(d_edges_joined))


if __name__ == "__main__":
    question_2_4()
