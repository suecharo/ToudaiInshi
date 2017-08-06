# coding: utf-8
import re


def read_line():
    while True:
        ret = input()
        if re.match(r"^.*([^a-z|&|\+|\!|\(|\)]).*$", ret):
            print("Please input only a-z or & or + or ! or ( or )")
            continue
        else:
            break

    return ret


def find_all_val(read):
    ret_set = set()
    for ele in read:
        if ele == "!" or ele == "&" or ele == "+" or ele == "(" or ele == ")":
            continue
        ret_set.add(ele)
    ret_list = sorted(list(ret_set))

    return ret_list


def change_read_to_sentence(read):
    sen_eval = []
    for ele in read:
        if ele == "&":
            sen_eval.append("and")
        elif ele == "!":
            sen_eval.append("not")
        elif ele == "+":
            sen_eval.append("or")
        else:
            sen_eval.append(ele)
    sen_eval = " ".join(sen_eval)

    return sen_eval


def do_excution_expand(sen_eval, l_all_val):
    ret_ans = []
    for n in range(2 ** len(l_all_val)):
        ans_val = []
        for i in range(len(l_all_val)):
            if n >> i & 1 == 1:
                ans_val.append(l_all_val[i] + "=true")
                val = l_all_val[i] + " = True"
            else:
                ans_val.append(l_all_val[i] + "=false")
                val = l_all_val[i] + " = False"
            exec(val)
        if eval(sen_eval):
            ret_ans.append(" ".join(ans_val))

    return ret_ans


def question_4():
    read = read_line()
    l_all_val = find_all_val(read)
    sen_eval = change_read_to_sentence(read)
    ans = do_excution_expand(sen_eval, l_all_val)
    if len(ans) == 0:
        print("none")
    else:
        print("\n".join(ans))


if __name__ == "__main__":
    question_4()
