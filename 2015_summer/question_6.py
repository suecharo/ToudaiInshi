# coding: utf-8
def calc_pair(pre, next):
    dp = [[0] * 20 for __ in range(20)]
    for i in range(20):
        dp[0][i] = i
        dp[i][0] = i

    for x in range(1, 20):
        for y in range(1, 20):
            if pre[x - 1] == next[y - 1]:
                score_fit = dp[x - 1][y - 1]
            else:
                score_fit = dp[x - 1][y - 1] + 1
            score_1 = dp[x - 1][y] + 1
            score_2 = dp[x][y - 1] + 1
            dp[x][y] = min(score_fit, score_1, score_2)

    return dp[19][19]


def question_6():
    f = open("program.txt", "r")
    file_text = f.read()
    l_line = file_text.split("\n")
    l_line_changed = []
    for line in l_line:
        if line == "":
            continue
        if len(line) >= 20:
            continue
        l_line_changed.append(line + " " * (19 - len(line)))

    count_pair = 0

    for i in range(0, len(l_line_changed) - 1):
        for j in range(i + 1, len(l_line_changed)):
            pre_line = l_line_changed[i]
            next_line = l_line_changed[j]
            if pre_line == next_line:
                continue

            score = calc_pair(pre_line, next_line)

            if score <= 4:
                count_pair += 1
                print(pre_line)
                print(next_line)
                print("-" * 40)

    print("count_pair : {}".format(count_pair))


if __name__ == "__main__":
    question_6()
