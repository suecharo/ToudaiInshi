# coding: utf-8
from question_3 import parse_read
from question_3 import do_exe


def question_4():
    f = open("prog4.txt", "r")
    read = f.open()
    f.close()

    d_line = parse_read(read)
    d_val = defaultdict(int)
    now_line = 0
    while len(d_line) > now_line >= 0:
        l_operater = d_line[now_line]
        next_line, d_val = do_exe(now_line, l_operater, d_val)
        now_line = next_line


if __name__ == "__main__":
    question_4()
