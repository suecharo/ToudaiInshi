# coding: utf-8
from question_4 import read_line
from question_4 import find_all_val
from question_4 import change_read_to_sentence
from question_4 import do_excution_expand


def change_ans_to_dnf(l_ans):
    ret_dnf = []
    for ans in l_ans:
        dnf_ans = []
        for ele in ans.split(" "):
            left_ele, right_ele = ele.split("=")
            if right_ele == "true":
                dnf_ans.append(left_ele)
            else:
                dnf_ans.append("!" + left_ele)
        ret_dnf.append("&".join(dnf_ans))
    ret_dnf = "+".join(ret_dnf)

    return ret_dnf


def question_5():
    read = read_line()
    l_all_val = find_all_val(read)
    sen_eval = change_read_to_sentence(read)
    l_ans = do_excution_expand(sen_eval, l_all_val)
    if len(l_ans) == 0:
        print("none")
    else:
        DNF = change_ans_to_dnf(l_ans)
        print(DNF)


if __name__ == "__main__":
    question_5()
