# coding: utf-8
from question_1 import read_num

def question_6():
    num = read_num()
    dp = [1] * (num + 1)
    for i in range(1, num + 1):
        dp[i] = (103515245 * dp[i - 1] + 12345) % (2 ** 26)

    k = 0
    purpose = dp[num]
    cache = dp[num]
    while True:
        k += 1
        cache = (103515245 * cache + 12345) % (2 ** 26)
        if purpose == cache:
            break

    print(k)


if __name__ == "__main__":
    question_6()
