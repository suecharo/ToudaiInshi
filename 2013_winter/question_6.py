# coding: utf-8
from question_4 import read_line
from question_4 import find_all_val
from question_4 import change_read_to_sentence
from question_4 import do_excution_expand


def change_ans_to_cnf(l_ans):
    ret_cnf = []
    for ans in l_ans:
        cnf_ans = []
        for ele in ans.split(" "):
            left_ele, right_ele = ele.split("=")
            if right_ele == "true":
                cnf_ans.append("!" + left_ele)
            else:
                cnf_ans.append(left_ele)
        cnf_ans = "(" + "+".join(cnf_ans) + ")"
        ret_cnf.append(cnf_ans)
    ret_cnf = "&".join(ret_cnf)

    return ret_cnf


def question_6():
    read = read_line()
    l_all_val = find_all_val(read)
    sen_eval = change_read_to_sentence(read)
    l_ans = do_excution_expand(sen_eval, l_all_val)
    if len(l_ans) == 0:
        print("none")
    else:
        CNF = change_ans_to_cnf(l_ans)
        print(CNF)


if __name__ == "__main__":
    question_6()
