# coding: utf-8
def read_num():
    try:
        num_input = input()
        chack_int = int(num_input)
        ret = list(map(int, list(num_input)))
    except:
        print("Please input only int.")
        ret = None
    return ret


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
    while True:
        input_num = read_num()
        if input_num is None:
            continue
        else:
            break

    print_text = ["", "", "", "", ""]

    for i, a_num in enumerate(input_num):
        char_text = change_num_to_char(a_num)
        if i == 0:
            for j in range(5):
                print_text[j] += char_text[j]
        else:
            for j in range(5):
                print_text[j] += "  "
                print_text[j] += char_text[j]

    write_text = "\n".join(print_text)
    # print(write_text)

    f = open("out1.txt", "w")
    f.write(write_text)
    f.close()


if __name__ == "__main__":
    question_1()
