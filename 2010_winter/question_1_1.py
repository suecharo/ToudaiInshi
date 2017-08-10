# coding: utf-8
import re

def read_file(text_name):
    f = open(text_name, "r")
    read = f.read()
    f.close()
    l_read = read.split("\n")
    ret = []
    for line in l_read:
        if re.search(r"^.*->.*$", line):
            ret.append(list(map(int, line.split("->"))))
        else:
            continue
    return ret


def question_1_1():
    l_edges = read_file("./data/a.txt")
    s_vertex = set()
    s_vertex.add(0)
    for v_x, v_y in l_edges:
        s_vertex.add(v_x)
        s_vertex.add(v_y)

    print(len(s_vertex))


if __name__ == "__main__":
    question_1_1()
