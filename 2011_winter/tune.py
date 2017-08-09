# coding: utf-8
import re
import random

class Game():
    def __init__(self):
        self.board = [["-"] * 3 for __ in range(3)] # [y][x]
        self.count = 0

    def start(self, pram_O, pram_X):
        while True:
            if self.count % 2 == 0:
                input_x, input_y = self.get_input_from_computer(pram_O)
            else:
                input_x, input_y = self.get_input_from_computer(pram_X)
            self.input_board(input_x, input_y)
            all_lines = self.make_all_lines()
            if self.check_win(all_lines):
                if self.count % 2 == 0:
                    return "O"
                else:
                    return "X"
                break
            self.count += 1
            if self.count == 9:
                return "-"

    def get_input_from_computer(self, pram):
        l_score = []
        l_brank = self.find_brank()
        for x, y in l_brank:
            if self.count % 2 == 0:
                self.board[y][x] = "O"
            else:
                self.board[y][x] = "X"
            score = self.calc_score(pram)
            l_score.append([score, (x, y)])
            self.board[y][x] = "-"
        l_score.sort(key=lambda x: -x[0])
        return l_score[0][1][0], l_score[0][1][1]

    def calc_score(self, pram):
        all_lines = self.make_all_lines()
        count_win = 0
        count_my_1 = 0
        count_my_2 = 0
        count_enemy_1 = 0
        count_enemy_2 = 0
        count_my_enemy = 0
        count_used = 0
        count_nothing = 0
        for line in all_lines:
            if self.count % 2 == 0:
                if line == "OOO":
                    count_win += 1
                elif line == "---":
                    count_nothing += 1
                elif re.match(r"O*-O*-O*$", line):
                    count_my_1 += 1
                elif re.match(r"O*-O*$", line):
                    count_my_2 += 1
                elif re.match(r"X*-X*-X*$", line):
                    count_my_1 += 1
                elif re.match(r"X*-X*$", line):
                    count_my_2 += 1
                elif re.match(r"[OX]*-[OX]*$", line):
                    count_my_enemy += 1
                else:
                    count_used += 1
            else:
                if line == "XXX":
                    count_win += 1
                elif line == "---":
                    count_nothing += 1
                elif re.match(r"X*-X*-X*$", line):
                    count_my_1 += 1
                elif re.match(r"X*-X*$", line):
                    count_my_2 += 1
                elif re.match(r"O*-O*-O*$", line):
                    count_my_1 += 1
                elif re.match(r"O*-O*$", line):
                    count_my_2 += 1
                elif re.match(r"[OX]*-[OX]*$", line):
                    count_my_enemy += 1
                else:
                    count_used += 1
        score = 0
        vector = [count_win, count_my_1, count_my_2, count_enemy_1, count_enemy_2, count_my_enemy, count_used, count_nothing]
        for v, p in zip(pram, vector):
            score += v * p
        return score

    def input_board(self, input_x, input_y):
        if self.count % 2 == 0:
            self.board[input_y][input_x] = "O"
        else:
            self.board[input_y][input_x] = "X"
        return True

    def make_all_lines(self):
        line_1 = "".join(self.board[0])
        line_2 = "".join(self.board[1])
        line_3 = "".join(self.board[2])
        line_A = "".join([self.board[0][0], self.board[1][0], self.board[2][0]])
        line_B = "".join([self.board[0][1], self.board[1][1], self.board[2][1]])
        line_C = "".join([self.board[0][2], self.board[1][2], self.board[2][2]])
        line_right = "".join([self.board[0][0], self.board[1][1], self.board[2][2]])
        line_left = "".join([self.board[0][2], self.board[1][1], self.board[2][0]])
        all_lines = [line_1, line_2, line_3, line_A, line_B, line_C, line_right, line_left]
        return all_lines

    def check_win(self, all_lines):
        for line in all_lines:
            if line == "OOO":
                return True
            elif line == "XXX":
                return True
        return False

    def find_brank(self):
        l_brank = []
        for y, row in enumerate(self.board):
            for x, ele in enumerate(row):
                if ele == "-":
                    l_brank.append((x, y))
        return l_brank

def make_pram():
    pram = [random.random() for __ in range(8)]
    return pram

def be_half(l_pram):
    ret_list = []
    for i in range(len(l_pram) // 2):
        p_1, p_2 = l_pram[i * 2], l_pram[i * 2 + 1]
        game_1, game_2 = Game(), Game()
        res_1 = game_1.start(p_1, p_2)
        res_2 = game_2.start(p_2, p_1)
        if res_1 == "O" and res_2 == "X":
            ret_list.append(p_1)
        elif res_1 == "O" and res_2 == "-":
            ret_list.append(p_1)
        elif res_1 == "O" and res_2 == "O":
            ret_list.append(p_1)
        elif res_1 == "-" and res_2 == "X":
            ret_list.append(p_1)
        elif res_1 == "-" and res_2 == "-":
            ret_list.append(p_1)
        elif res_1 == "-" and res_2 == "O":
            ret_list.append(p_2)
        elif res_1 == "X" and res_2 == "X":
            ret_list.append(p_1)
        elif res_1 == "X" and res_2 == "-":
            ret_list.append(p_2)
        elif res_1 == "X" and res_2 == "O":
            ret_list.append(p_2)
    return ret_list

def fight_128():
    lst = [make_pram() for __ in range(128)]
    for __ in range(7):
        lst = be_half(lst)
    return lst[0]

def fight_128_128():
    print(1)
    lst = [fight_128() for __ in range(128)]
    for __ in range(7):
        lst = be_half(lst)
    return lst[0]

def tune():
    lst = [fight_128_128() for __ in range(128)]
    for __ in range(7):
        lst = be_half(lst)
    print(lst[0])

if __name__ == "__main__":
    tune()
