# coding: utf-8
from question_1 import change_num_to_char
from question_1 import write_file


def read_str():
    read_str = input()
    if re.search(r"[^\d,]", read_str):
        print("Input only num or ,.")
        return read_num()
    return read_str


def draw_print_num(drow_num, l_pos, l_margin):
    max_pos = max(l_pos)
    print_text = [""] * (5 + max_pos)
    for i, num in enumerate(drow_num):
        num = int(num)
        pos = l_pos[i]
        num_char = change_num_to_char(num)
        for j in range(max_pos + 5):
            if pos <= j <= pos + 4:
                print_text[j] += num_char[j - pos]
            else:
                if num == 1:
                    print_text[j] += " "
                else:
                    print_text[j] += " " * 4
        if i != len(drow_num) - 1:
            for j in range(max_pos + 5):
                print_text[j] += " " * l_margin[i]
    ret_text = "\n".join(print_text)
    return ret_text


def question_3():
    input_str = read_str()
    # input_str = "813,0,4,1,3,2"
    l_input = input_str.split(",")
    drow_num = l_input[0]
    l_pos = list(map(int, l_input[1::2]))
    l_margin = list(map(int, l_input[2::2]))
    print_text = draw_print_num(drow_num, l_pos, l_margin)
    # print(print_text)
    write_file("out3.txt", print_text)


if __name__ == "__main__":
    question_3()
