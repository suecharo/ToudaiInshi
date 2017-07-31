# coding: utf-8
import re
def change_roman_to_arabic(roman_num):
    arabic_num = 0
    for ind, char in enumerate(roman_num):
        num = 0
        if char == "I":
            num = 1
        elif char == "V":
            num = 5
        elif char == "X":
            num = 10
        elif char == "L":
            num = 50
        elif char == "C":
            num = 100
        elif char == "D":
            num = 500
        elif char == "M":
            num = 1000

        if ind != len(roman_num) - 1:
            next_char = roman_num[ind + 1]
            if char == "I" and next_char == "V":
                num *= -1
            elif char == "I" and next_char == "X":
                num *= -1
            elif char == "X" and next_char == "L":
                num *= -1
            elif char == "X" and next_char == "C":
                num *= -1
            elif char == "C" and next_char == "D":
                num *= -1
            elif char == "C" and next_char == "M":
                num *= -1

        arabic_num += num

    return arabic_num


def question_3():
    while True:
        input_str = input()
        if re.match(r"^.*[^I|V|X|L|C|D|M].*$", input_str):
            print("Please input only abcdefgh")
        else:
            break

    arabic_num = change_roman_to_arabic(input_str)
    print(arabic_num)


if __name__ == "__main__":
    question_3()
