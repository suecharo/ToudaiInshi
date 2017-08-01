# coding: utf-8
import re

def question_2():
    f = open("program.txt", "r")
    read_file = f.read()
    l_line = read_file.split("\n")
    re_main = re.compile(r"^.*(main).*$")
    for ind, line in enumerate(l_line):
        if re_main.match(line):
            print("{} : {}".format(ind + 1, line))


if __name__ == "__main__":
    question_2()
