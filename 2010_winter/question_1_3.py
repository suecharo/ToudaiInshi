# coding: utf-8
from question_1_1 import read_file
from collections import defaultdict
from copy import copy


# def make_all_VAR(l_edges):
#     d_edges = defaultdict(list)
#     V = [set()]
#     V[0].add(0)
#     A = [set()]
#     R = [set()]
#     R[0].add(0)
#     for t in range(len(l_edges)):
#         print(t)
#         edge = l_edges[t]
#         v_x, v_y = edge
#         d_edges[v_x].append(v_y)
#         now_V = V[t]
#         now_A = A[t]
#         now_R = R[t]
#
#         next_V = copy(now_V)
#         next_V.add(v_x)
#         next_V.add(v_y)
#         next_A = copy(now_A)
#         next_A.add(tuple(edge))
#         next_R = copy(now_R)
#         if v_x in now_R and v_y not in now_R:
#             next_R.add(v_y)
#             queue = d_edges[v_y]
#             while len(queue) != 0:
#                 next_queue = []
#                 for v in queue:
#                     if v in next_R:
#                         continue
#                     else:
#                         next_R.add(v)
#                         for ele in d_edges[v]:
#                             next_queue.append(ele)
#                 queue = next_queue
#
#         V.append(next_V)
#         A.append(next_A)
#         R.append(next_R)
#
#     return V, A, R


def setup_VAR():
    V, A, R = set(), set(), set()
    V.add(0)
    R.add(0)

    return V, A, R


def update_VAR(edge, d_edges, pre_V, pre_A, pre_R):
    v_x, v_y = edge
    d_edges[v_x].add(v_y)
    now_V = copy(pre_V)
    now_A = copy(pre_A)
    now_R = copy(pre_R)
    now_V.add(v_x)
    now_V.add(v_y)
    now_A.add(tuple(edge))
    if v_x in pre_R and v_y not in pre_R:
        now_R.add(v_y)
        queue = d_edges[v_y]
        while len(queue) != 0:
            next_queue = []
            for v in queue:
                if v in now_R:
                    continue
                else:
                    now_R.add(v)
                    for ele in d_edges[v]:
                        next_queue.append(ele)
            queue = next_queue

    return d_edges, now_V, now_A, now_R


def question_1_3():
    l_edges = read_file("./data/a.txt")
    pre_V, pre_A, pre_R = setup_VAR()
    d_edges = defaultdict(set)
    t_v = False
    t_r = False
    for t in range(1, len(l_edges)):
        if t_v and t_r:
            break
        edge = l_edges[t - 1]
        d_edges, now_V, now_A, now_R = update_VAR(edge, d_edges, pre_V, pre_A, pre_R)
        if t_v is False:
            if len(pre_V) < 1000 and len(now_V) >= 1000:
                print("t_v : {}".format(t))
                t_v = True
        if t_r is False:
            if len(pre_R) < 1000 and len(now_R) >= 1000:
                print("t_r : {}".format(t))
                t_r = True
        pre_V, pre_A, pre_R = now_V, now_A, now_R


if __name__ == "__main__":
    question_1_3()
