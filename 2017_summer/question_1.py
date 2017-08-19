# coding: utf-8
import re

def write_file(text_name, write_text):
    f = open(text_name, "w")
    f.write(write_text)
    f.close()
    return True


def read_num():
    read_str = input()
    if re.search(r"[^\d,]", read_str):
        print("Input only num.")
        return read_num()
    return read_str


def change_num_to_char(num):
    if num == 0:
        ret_text = ["****",
                    "|  |",
                    "*  *",
                    "|  |",
                    "****"]
    elif num == 1:
        ret_text = ["*",
                    "|",
                    "*",
                    "|",
                    "*"]
    elif num == 2:
        ret_text = ["****",
                    "   |",
                    "****",
                    "|   ",
                    "****"]
    elif num == 3:
        ret_text = ["****",
                    "   |",
                    "****",
                    "   |",
                    "****"]
    elif num == 4:
        ret_text = ["*  *",
                    "|  |",
                    "****",
                    "   |",
                    "   *"]
    elif num == 5:
        ret_text = ["****",
                    "|   ",
                    "****",
                    "   |",
                    "****"]
    elif num == 6:
        ret_text = ["*   ",
                    "|   ",
                    "****",
                    "|  |",
                    "****"]
    elif num == 7:
        ret_text = ["****",
                    "   |",
                    "   *",
                    "   |",
                    "   *"]
    elif num == 8:
        ret_text = ["****",
                    "|  |",
                    "****",
                    "|  |",
                    "****"]
    elif num == 9:
        ret_text = ["****",
                    "|  |",
                    "****",
                    "   |",
                    "   *"]
    return ret_text


def question_1():
    input_num = read_num()
    print(input_num)
    # print_text = ["", "", "", "", ""]
    # for i, char_num in enumerate(input_num):
    #     char_text = change_num_to_char(int(char_num))
    #     if i == 0:
    #         for j in range(5):
    #             print_text[j] += char_text[j]
    #     else:
    #         for j in range(5):
    #             print_text[j] += " " * 2
    #             print_text[j] += char_text[j]
    # write_text = "\n".join(print_text)
    # print(write_text)
    # write_file("out1.txt", write_text)


if __name__ == "__main__":
    question_1()
