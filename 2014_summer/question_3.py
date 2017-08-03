# coding: utf-8
import math

def question_3():
    ans = 0
    tri = (10 * 10 * math.sqrt(3)) / 2
    for n in range(3):
        if n == 0:
            ans += tri
        elif n == 1:
            ans += 3 * tri / 9
        else:


1
3 6
12 18
36 48


if __name__ == "__main__":
    question_3()
