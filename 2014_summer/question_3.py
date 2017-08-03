# coding: utf-8
import math

def question_3():
    ans = 0
    s_0 = 25 * math.sqrt(3)
    for i in range(3):
        if i == 0:
            ans += s_0
        else:
            tri_num = 3 * (4 ** (i - 1))
            s_i = s_0 * ((1 / 9) ** i)
            ans += s_i * tri_num

    print(ans)


if __name__ == "__main__":
    question_3()
