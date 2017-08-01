# coding: utf-8
from collections import defaultdict


def question_7():
    f = open("program.txt", "r")
    file_text = f.read()
    l_line = file_text.split("\n")
    l_id = [0] * len(l_line)
    d_line_id = defaultdict(int)
    id = 0
    for ind, line in enumerate(l_line):
        if line in d_line_id:
            l_id[ind] = d_line_id[line]
        else:
            d_line_id[line] = id
            id += 1

    s_printed = set()
    for i in range(len(l_line) - 3):
        lines_id = l_id[i] * (id ** 3) + l_id[i + 1] * (id ** 2) + l_id[i + 2] * id + l_id[i + 3]
        if lines_id in s_printed:
            continue
        else:
            s_printed.add(lines_id)
            print("\n".join(l_line[i:i + 4]))
            print("-" * 40)


if __name__ == "__main__":
    question_7()
