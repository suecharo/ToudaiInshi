# coding: utf-8
from question_2 import read


def make_dict(read_file):
    d_words = dict()
    for i in range(len(read_file) - 5):
        word = read_file[i:i+6]
        if word in d_words:
            continue
        else:
            d_words[word] = f"{i:0>3}"

    return d_words


def question_3():
    s_1 = read("./data/s1.txt")
    d_words = make_dict(s_1)
    print(len(d_words.keys()))


if __name__ == "__main__":
    question_3()
