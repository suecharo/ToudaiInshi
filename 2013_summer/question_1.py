# coding: utf-8
def question_1():
    f = open("prog1.txt", "r")
    read = f.read()
    f.close()

    l_read = read.split("\n")
    for line in l_read:
        l_line = line.split(" ")
        print(l_line[1])


if __name__ == "__main__":
    question_1()
