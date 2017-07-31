# coding: utf-8
def read():
    num = input()
    try:
        num = int(num)
    except:
        print("Please input only int.")
        num = None
    return num


def change_4_to_10(num):
    ret_num = ""
    mod = num
    while mod >= 4:
        div, mod = divmod(mod, 4)
        ret_num += str(div)
    else:
        ret_num += str(mod)

    return ret_num


def question_1():
    num = None
    while num is None:
        num = read()

    print_num = change_4_to_10(num)
    print(print_num)


if __name__ == "__main__":
    question_1()
