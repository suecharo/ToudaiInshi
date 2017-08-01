# coding: utf-8
def question_5():
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
            count_wrong = 0
            for p, n in zip(pre_line, next_line):
                if p != n:
                    count_wrong += 1
                if count_wrong == 5:
                    break
            else:
                count_pair += 1
                print(pre_line)
                print(next_line)
                print("-" * 40)

    print("count_pair : {}".format(count_pair))


if __name__ == "__main__":
    question_5()
