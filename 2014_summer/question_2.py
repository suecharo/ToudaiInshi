# coding: utf-8
from question_1 import read_float

def calc_r0(num):
    p_q = 0
    while True:
        if num * p_q <= 10:
            p_q += 1
        else:
            break

    return p_q * p_q


def calc_r1(num):
    div = int(10 / num)
    count = 0
    for x in range(div + 1):
        for y in range(div + 1):
            if (x - 5) ** 5 + (y - 5) ** 5 <= 25:
                count += 1

    return count


def question_2():
    float_num = read_float()
    r0 = calc_r0(float_num)
    r1 = calc_r1(float_num)
    ans = r1 / (r0 * 4)
    print(ans)


if __name__ == "__main__":
    question_2()
