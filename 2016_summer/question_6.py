# coding: utf-8
from question_5 import change_arabic_to_roman

def read():
    num = input()
    try:
        num = int(num)
    except:
        print("Please input only int.")
        num = None
    return num


def change_arabic_to_roman_expand(arabic_num):
    roman_num = ""

    if len(str(arabic_num)) == 4:
        under_3 = int(str(arabic_num)[1:4])
        upper_1 = int(str(arabic_num)[0])
        roman_num += "M" * upper_1
        if under_3 == 999:
            roman_num += "IM"
        elif under_3 == 995:
            roman_num += "VM"
        elif under_3 == 990:
            roman_num += "XM"
        elif under_3 == 950:
            roman_num += "LM"
        elif under_3 == 499:
            roman_num += "ID"
        elif under_3 == 495:
            roman_num += "VD"
        elif under_3 == 490:
            roman_num += "XD"
        elif under_3 == 450:
            roman_num += "LD"
        else:
            roman_num = change_arabic_to_roman(roman_num)

    elif len(str(arabic_num)) == 3:
        under_2 = int(str(arabic_num)[1:3])
        upper_1 = str(arabic_num)[0]

        if upper_1 == "1":
            roman_num += "C"
        elif upper_1 == "2":
            roman_num += "CC"
        elif upper_1 == "3":
            roman_num += "CCC"
        elif upper_1 == "4":
            roman_num += "CD"
        elif upper_1 == "5":
            roman_num += "D"
        elif upper_1 == "6":
            roman_num += "DC"
        elif upper_1 == "7":
            roman_num += "DCC"
        elif upper_1 == "8":
            roman_num += "DCCC"
        elif upper_1 == "9":
            roman_num += "CM"

        if under_2 == 99:
            roman_num += "IC"
        elif under_2 == 95:
            roman_num += "VC"
        elif under_2 == 49:
            roman_num += "IL"
        elif under_2 == 45:
            roman_num += "IV"
        else:
            roman_num = change_arabic_to_roman(roman_num)
    else:
        roman_num = change_arabic_to_roman(roman_num)

    return roman_num


def question_6():
    arabic_num = None
    while arabic_num is None:
        arabic_num = read()

    roman_num = change_arabic_to_roman_expand(arabic_num)
    print(roman_num)


if __name__ == "__main__":
    question_6()
