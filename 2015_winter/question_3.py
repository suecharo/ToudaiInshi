# coding: utf-8
def question_3():
    dp = [1] * 100
    for i in range(1, 100):
        dp[i] = (161 * dp[i - 1] + 2457) % (2 ** 24)

    count = 0
    for i in range(1, 100, 2):
        num = dp[i]
        if num % 2 == 0:
            count += 1

    print(count)


if __name__ == "__main__":
    question_3()
