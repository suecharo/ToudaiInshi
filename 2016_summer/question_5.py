# coding: utf-8
from collections import deque

def read():
    num = input()
    try:
        num = int(num)
    except:
        print("Please input only int.")
        num = None
    return num


def change_arabic_to_roman(arabic_num):
    roman_num = deque()
    for ind, char in enumerate(reversed(str(arabic_num))):
        add_roman = ""
        if ind == 3:
            add_roman = "M" * int(char)
        elif ind == 2:
            if char == "1":
                add_roman = "C"
            elif char == "2":
                add_roman = "CC"
            elif char == "3":
                add_roman = "CCC"
            elif char == "4":
                add_roman = "CD"
            elif char == "5":
                add_roman = "D"
            elif char == "6":
                add_roman = "DC"
            elif char == "7":
                add_roman = "DCC"
            elif char == "8":
                add_roman = "DCCC"
            elif char == "9":
                add_roman = "CM"
        elif ind == 1:
            if char == "1":
                add_roman = "X"
            elif char == "2":
                add_roman = "XX"
            elif char == "3":
                add_roman = "XXX"
            elif char == "4":
                add_roman = "XL"
            elif char == "5":
                add_roman = "L"
            elif char == "6":
                add_roman = "LX"
            elif char == "7":
                add_roman = "LXX"
            elif char == "8":
                add_roman = "LXXX"
            elif char == "9":
                add_roman = "XC"
        elif ind == 0:
            if char == "1":
                add_roman = "I"
            elif char == "2":
                add_roman = "II"
            elif char == "3":
                add_roman = "III"
            elif char == "4":
                add_roman = "IV"
            elif char == "5":
                add_roman = "V"
            elif char == "6":
                add_roman = "VI"
            elif char == "7":
                add_roman = "VII"
            elif char == "8":
                add_roman = "VIII"
            elif char == "9":
                add_roman = "IX"
        roman_num.appendleft(add_roman)

    roman_num = "".join(list(roman_num))
    return roman_num


def question_5():
    arabic_num = None
    while arabic_num is None:
        arabic_num = read()

    roman_num = change_arabic_to_roman(arabic_num)
    print(roman_num)


if __name__ == "__main__":
    question_5()
