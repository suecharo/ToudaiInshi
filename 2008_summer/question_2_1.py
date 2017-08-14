# coding: utf-8
from collections import defaultdict


def read_file():
    f = open("edges.txt", "r")
    read = f.read()
    f.close()
    read = read.split("\n")
    return read


def make_d_edges(read, num):
    d_edges = defaultdict(set)
    for i in range(num):
        a, b = map(int, read[i].split(" "))
        d_edges[a].add(b)
        d_edges[b].add(a)
    return d_edges


def find_joined_graph(d_edges):
    s_all_ver = set(range(1, 101))
    s_used_ver = {1}
    s_graph = {1}
    queue = [1]
    graph_all_set = []
    while True:
        while len(queue) != 0:
            next_queue = []
            for ele in queue:
                next_ver = d_edges[ele]
                for n_ele in next_ver:
                    if n_ele in s_used_ver:
                        continue
                    else:
                        s_graph.add(n_ele)
                        s_used_ver.add(n_ele)
                        next_queue.append(n_ele)
            queue = next_queue
        graph_all_set.append(s_graph)
        if len(s_used_ver) == 100:
            break
        else:
            ele = list(s_all_ver - s_used_ver)[0]
            s_used_ver.add(ele)
            s_graph = {ele}
            queue = [ele]
    return graph_all_set


def question_2_1():
    l_read = read_file()
    d_edges = make_d_edges(l_read, 181)
    joined_ver = find_joined_graph(d_edges)
    for i in joined_ver:
        print(len(i))


if __name__ == "__main__":
    question_2_1()
