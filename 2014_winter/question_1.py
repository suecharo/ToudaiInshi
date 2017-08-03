# coding: utf-8
def calc_f(num):
    if num <= 2:
        return 1
    else:
        dp = [1] * (num + 1)
        for i in range(3, num + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

    return dp[num]


def question_1():
    num = 10
    ans = calc_f(num)
    print(ans)


if __name__ == "__main__":
    question_1()
