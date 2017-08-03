# coding: utf-8
import math
import re

def read_num():
    while True:
        input_num = input()
        if re.match(r"^.*(/D).*$", input_num):
            print("Please input only num.")
            continue
        else:
            if input_num == "0":
                print("Please input only positive num.")
                continue
            else:
                input_num = int(input_num)
                break

    return input_num



def question_4():
    n = read_num()
    K_n = 0
    s_0 = 25 * math.sqrt(3)
    for i in range(n + 1):
        if i == 0:
            K_n += s_0
        else:
            tri_num = 3 * (4 ** (i - 1))
            s_i = s_0 / (9 ** i)
            K_n += s_i * tri_num

    print(K_n)


if __name__ == "__main__":
    question_4()
