# coding: utf-8
from question_1 import change_num_to_char

def question_3():
    input_str = str(input())
    # input_str = "813,0,4,1,3,2"
    l_input = input_str.split(",")
    drow_num = l_input[0]
    l_pos = list(map(int, l_input[1::2]))
    l_margin = list(map(int, l_input[2::2]))

    max_pos = max(l_pos)
    print_text = [""] * (5 + max_pos)

    for i, num in enumerate(drow_num):
        num = int(num)
        pos = l_pos[i]
        num_char = change_num_to_char(num)
        if i == len(drow_num) - 1:
            if num == 1:
                for i in range(pos):
                    print_text[i] += " "
                for i in range(5):
                    print_text[pos + i] += num_char[i]
                for i in range(pos + 5, max_pos + 5):
                    print_text[i] += " "
            else:
                for i in range(pos):
                    print_text[i] += " " * 4
                for i in range(5):
                    print_text[pos + i] += num_char[i]
                for i in range(pos + 5, max_pos + 5):
                    print_text[i] += " " * 4
        else:
            margin = l_margin[i]
            if num == 1:
                for i in range(pos):
                    print_text[i] += " "
                for i in range(5):
                    print_text[pos + i] += num_char[i]
                for i in range(pos + 5, max_pos + 5):
                    print_text[i] += " "
            else:
                for i in range(pos):
                    print_text[i] += " " * 4
                for i in range(5):
                    print_text[pos + i] += num_char[i]
                for i in range(pos + 5, max_pos + 5):
                    print_text[i] += " " * 4
            for i in range(max_pos + 5):
                print_text[i] += " " * margin

    write_text = "\n".join(print_text)
    print(write_text)

    f = open("out3.txt", "w")
    f.write(write_text)
    f.close()


if __name__ == "__main__":
    question_3()
