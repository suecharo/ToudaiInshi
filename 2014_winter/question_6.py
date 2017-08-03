# coding: utf-8
from decimal import *
my_context = Context(prec=32, rounding=ROUND_HALF_DOWN)
setcontext(my_context)

def question_6():
    phai = (Decimal(1) + (Decimal("5") ** Decimal("0.5"))) / Decimal("2")
    print(phai)


if __name__ == "__main__":
    question_6()
