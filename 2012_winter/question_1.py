# coding: utf-8
def question_1():
    f = open("data1.txt", "r")
    read = f.read()
    f.close()
    l_read = []
    for line in read.split("\n"):
        line = line[1:-1]
        x, y = map(int, line.split(","))
        l_read.append([x, y])
    ans = sorted(l_read, key=lambda x: -x[1])[0]
    print("(x, y) : ({} , {})".format(ans[0], ans[1]))


if __name__ == "__main__":
    question_1()
