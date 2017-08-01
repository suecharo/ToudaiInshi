# coding: utf-8
def question_1():
    f = open("program.txt", "r")
    read_file = f.read()
    count = 0
    for i in read_file:
        if i == ";":
            count += 1

    print(count)


if __name__ == "__main__":
    question_1()
