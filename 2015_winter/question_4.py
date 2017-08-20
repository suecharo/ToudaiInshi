# coding: utf-8
def question_4():
    dp = [1] * (10 ** 6 + 1)
    for i in range(1, 10 ** 6 + 1):
        dp[i] = (161 * dp[i - 1] + 2457) % (2 ** 24)

    print(dp[10 ** 6])
    # print(dp)


if __name__ == "__main__":
    question_4()
