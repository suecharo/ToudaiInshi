# coding: utf-8
import re

def read_num():
    while True:
        read_num = input()
        read_num = read_num.split(" ")
        if len(read_num) != 2:
            print("Please input space.")
            continue
        else:
            num_front = read_num[0]
            num_back = read_num[1]
            if len(num_front) != 32 or re.match(r"^.*(/D).*$", num_front) or len(num_back) != 2 or re.match(r"^.*(/D).*$", num_back):
                print("Please input only 32 2_num.")
                continue
            else:
                break
    return read_num


def calc_mult_float(num_1, num_2):
    num_1_front, num_1_back = map(int, num_1)
    num_2_front, num_2_back = map(int, num_2)

    mult = num_1_front * num_2_front
    sum_back = num_1_back + num_2_back
    mult_len = len(str(mult))
    all_disit_sum = sum_back + mult_len - 63
    if all_disit_sum >= 0:
        if all_disit_sum >= 10:
            ret_back = str(all_disit_sum)
        else:
            ret_back = "0{}".format(all_disit_sum)

        if mult_len >= 32:
            ret_front = str(mult)[:32]
        else:
            ret_front = str(mult) + "0" * (32 - mult_len)

    else:
        ret_back = "00"
        dif = abs(all_disit_sum)
        if dif < 32:
            ret_front = "0" * dif + str(mult)[:32 - dif]
        else:
            ret_front = "0" * 32

    return "{} {}".format(ret_front, ret_back)


def question_5():
    print("Please input num_1.")
    num_1 = read_num()
    print("Please input num_2.")
    num_2 = read_num()

    ans = calc_mult_float(num_1, num_2)

    print("-" * 3 + " ans " + "-" * 37)
    print(ans)


if __name__ == "__main__":
    question_5()
