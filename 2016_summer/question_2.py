# coding: utf-8
import re
def change_8_to_10(num_str):
    ret_num = 0
    for ind, char in enumerate(reversed(num_str)):
        num = None
        if char == "a":
            num = 0
        elif char == "b":
            num = 1
        elif char == "c":
            num = 2
        elif char == "d":
            num = 3
        elif char == "e":
            num = 4
        elif char == "f":
            num = 5
        elif char == "g":
            num = 6
        elif char == "h":
            num = 7
        ret_num += num * (8 ** ind)

    return ret_num


def question_2():
    while True:
        input_str = input()
        if re.match(r"^.*[^a-h].*$", input_str):
            print("Please input only abcdefgh")
        else:
            break

    print_num = change_8_to_10(input_str)
    print(print_num)


if __name__ == "__main__":
    question_2()
