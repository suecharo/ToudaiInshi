# coding: utf-8
from collections import defaultdict

def question_4():
    f = open("program.txt", "r")
    file_text = f.read()
    l_line = file_text.split("\n")
    d_info = defaultdict(lambda :[None, 1]) # first appear, count
    for ind, line in enumerate(l_line):
        if line in d_info:
            d_info[line][1] += 1
        else:
            d_info[line][0] = ind + 1

    ans = []
    all_count = 0
    for key, value in d_info.items():
        if value[1] < 2:
            continue
        else:
            ans.append((value[0], key))
            all_count += value[1]

    ans.sort(key= lambda x: x[0])
    for i in ans:
        print(i[1])


if __name__ == "__main__":
    question_4()
