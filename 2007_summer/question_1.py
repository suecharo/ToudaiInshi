# coding: utf-8
def read_file(text_name):
    f = open(text_name, "r")
    ret = f.read()
    f.close()
    return ret


def decode_sentence_caesar(sentense, num):
    ret = ""
    for i in range(len(sentense)):
        char = sentense[i]
        c_ord = ord(char)
        if 65 <= c_ord <= 90:
            c_ord = ((c_ord - 65 + num) % 26) + 65
            ret += chr(c_ord)
        elif 97 <= c_ord <= 122:
            c_ord = ((c_ord - 97 + num) % 26) + 97
            ret += chr(c_ord)
        else:
            ret += char

    return ret


def question_1():
    read = read_file("q1.txt")
    l_read = read.split("\n")
    key = 15
    print("-" * 40)
    print("key : {}".format(key))
    for row in l_read:
        print(decode_sentence_caesar(row, key))


if __name__ == "__main__":
    question_1()
