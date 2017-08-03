# coding: utf-8
from decimal import *
my_context = Context(prec=32, rounding=ROUND_HALF_DOWN)
setcontext(my_context)


def question_7():
    f = [None] * 141
    f[1], f[2] = Decimal(1), Decimal(1)
    for i in range(3, 141):
        f[i] = f[i - 1] + f[i - 2]

    g = [None] * 141
    sqrt_5 = (Decimal(5) ** Decimal("0.5"))
    phai = (Decimal(1) + sqrt_5) / Decimal(2)
    g[0] = Decimal(1) / sqrt_5
    for i in range(1, 141):
        g[i] = g[i - 1] * phai

    dif_abs = [abs(_f - _g) for _f, _g in zip(f[1:141], g[1:141])]
    ans = max(dif_abs)

    print(ans)
    print(g)


if __name__ == "__main__":
    question_7()
