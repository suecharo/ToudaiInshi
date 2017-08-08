# coding: utf-8
from question_2 import read


def compress(read_file):
    ret_str = ""
    d_words = dict()
    changed = False
    change_from = 0
    for i in range(len(read_file)):
        if i >= change_from + 6:
            changed = False

        if i < len(read_file) - 5:
            word = read_file[i:i+6]
            if word in d_words:
                if changed is False:
                    ret_str += d_words[word]
                    changed = True
                    change_from = i
            else:
                d_words[word] = f"{i:0>3}"
                if changed is False:
                    ret_str += read_file[i]
        else:
            if changed is False:
                ret_str += read_file[i]

    return ret_str


def question_4():
    s_1 = read("./data/s1.txt")
    s_2 = read("./data/s2.txt")
    str_com_1 = compress(s_1)
    str_com_2 = compress(s_2)
    print("s1.txt : len - {}, tail - {}".format(len(str_com_1), str_com_1[len(str_com_1) - 10:]))
    print("s2.txt : len - {}, tail - {}".format(len(str_com_2), str_com_2[len(str_com_2) - 10:]))


if __name__ == "__main__":
    question_4()
