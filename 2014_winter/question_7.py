# coding: utf-8
from decimal import *
my_context = Context(prec=32, rounding=ROUND_HALF_DOWN)
setcontext(my_context)

def calc_g(num):
    phai = (Decimal(1) + (Decimal("5") ** Decimal("0.5"))) / Decimal("2")
    g = (phai ** Decimal(num)) / (Decimal("5") ** Decimal("0.5"))
    return g


def question_7():
    num = 140
    print(calc_g(140))


if __name__ == "__main__":
    question_7()
