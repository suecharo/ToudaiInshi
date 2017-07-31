# coding: utf-8
import re

def change_word_to_arabic(word):
    if word == "one":
        return 1
    elif word == "two":
        return 2
    elif word == "three":
        return 3
    elif word == "four":
        return 4
    elif word == "five":
        return 5
    elif word == "six":
        return 6
    elif word == "seven":
        return 7
    elif word == "eight":
        return 8
    elif word == "nine":
        return 9
    elif word == "ten":
        return 10
    elif word == "eleven":
        return 11
    elif word == "twelve":
        return 12
    elif word == "thirteen":
        return 13
    elif word == "fourteen":
        return 14
    elif word == "fifteen":
        return 15
    elif word == "sixteen":
        return 16
    elif word == "seventeen":
        return 17
    elif word == "eighteen":
        return 18
    elif word == "nineteen":
        return 19
    elif word == "twenty":
        return 20
    elif word == "thirty":
        return 30
    elif word == "forty":
        return 40
    elif word == "fifty":
        return 50
    elif word == "sixty":
        return 60
    elif word == "seventy":
        return 70
    elif word == "eighty":
        return 80
    elif word == "ninety":
        return 90


def change_3_english_to_arabic(l_eng):
    s_eng = set(l_eng)
    ret_num = 0
    if "hundred" in s_eng:
        for ind, word in enumerate(l_eng):
            if ind == 0:
                ret_num += change_word_to_arabic(word) * 100
            elif ind == 1:
                continue
            else:
                ret_num += change_word_to_arabic(word)
    else:
        for word in s_eng:
            ret_num += change_word_to_arabic(word)

    return ret_num


def change_english_to_arabic(english):
    l_eng = english.split(" ")
    s_eng = set(l_eng)
    if "thousand" in s_eng:
        ind_thousand = 0
        for ind, word in enumerate(l_eng):
            if word == "thousand":
                ind_thousand = ind
                break
        ret_num = change_3_english_to_arabic(l_eng[:ind_thousand]) * 1000 + change_3_english_to_arabic(l_eng[ind_thousand + 1:])
    else:
        ret_num = change_3_english_to_arabic(l_eng)

    return ret_num


def question_7():
    input_str = input()
    arabic_num = change_english_to_arabic(input_str)
    print(arabic_num)


if __name__ == "__main__":
    question_7()
