# coding: utf-8
from question_1 import read_num

def question_5():
    num = read_num()
    dp = [1] * (num + 1)
    for i in range(1, num + 1):
        dp[i] = (1103515245 * dp[i - 1] + 12345) % (2 ** 26)

    print("input_num : {}",format(dp[num]))
    print("2 : {}", format(dp[2]))
    print("3 : {}", format(dp[3]))


if __name__ == "__main__":
    question_5()
