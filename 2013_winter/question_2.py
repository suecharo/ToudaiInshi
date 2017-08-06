# coding: utf-8
from question_1 import read_line


def find_all_val(read):
    l_read = read.split("+")
    ret_set = set()
    for line in l_read:
        ret_set.add(ele)
    ret_list = sorted(list(ret_set))

    return ret_list


def do_excution(l_read, l_all_val):
    ret_ans = []
    sen_eval = " or ".join(l_read)
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


def question_2():
    read = read_line()
    l_all_val = find_all_val(read)
    ans = do_excution(read, l_all_val)
    if len(ans) == 0:
        print("none")
    else:
        print("\n".join(ans))


if __name__ == "__main__":
    question_2()
