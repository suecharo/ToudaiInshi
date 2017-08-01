# coding: utf-8
def question_3():
    f = open("program.txt", "r")
    read_file = f.read()
    l_line = read_file.split("\n")
    for i in range(len(l_line) - 1):
        now_line = l_line[i]
        next_line = l_line[i + 1]
        if now_line == next_line:
            print(now_line)


if __name__ == "__main__":
    question_3()
