# coding: utf-8
import random
import re

class Game():
    def __init__(self):
        self.board = [["-"] * 3 for __ in range(3)] # [y][x]

    def start(self):
        print("*" * 3 + " Where Put?? " + "*" * 3)
        self.make_board()
        self.print_board()
        input_x, input_y = self.get_input_from_player()
        self.board[input_y][input_x] = "O"
        print("-" * 40)
        self.print_board()
        self.check_board()

    def make_board(self):
        while True:
            l_choice = [(x, y) for x in range(3) for y in range(3)]
            O_count, X_count = 0, 0
            while True:
                x_input, y_input = random.choice(l_choice)
                if self.board[y_input][x_input] != "-":
                    continue
                self.board[y_input][x_input] = "O"
                O_count += 1
                if O_count == 2:
                    break
            while True:
                x_input, y_input = random.choice(l_choice)
                if self.board[y_input][x_input] != "-":
                    continue
                self.board[y_input][x_input] = "X"
                X_count += 1
                if X_count == 2:
                    break
            all_lines = self.make_all_lines()
            if self.check_win(all_lines):
                self.__init__()
                continue
            else:
                break
        return True

    def check_win(self, all_lines):
        for line in all_lines:
            if line == "OOO":
                return True
            elif line == "OO-":
                return True
            elif line == "O-O":
                return True
            elif line == "-OO":
                return True
            elif line == "XXX":
                return True
        return False


    def get_input_from_player(self):
        print("You are O.")
        while True:
            print("Please input like [1-3][A-C].")
            line = input()
            if re.match(r"[1-3][A-C]$", line):
                input_y = int(line[0]) - 1
                if line[1] == "A":
                    input_x = 0
                elif line[1] == "B":
                    input_x = 1
                elif line[1] == "C":
                    input_x = 2
                if self.board[input_y][input_x] != "-":
                    print("You can not put here.")
                    continue
                else:
                    break
            else:
                continue
        return input_x, input_y

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

    def check_board(self):
        x_all_lines = self.make_all_lines()
        for line in x_all_lines:
            if re.match(r"X*-X*$", line):
                print("You will have to be lose.")
                return True
        l_brank = self.find_brank()
        count_win = 0
        count_draw = 0
        for x, y in l_brank:
            self.board[y][x] = "X"
            all_lines = self.make_all_lines()
            draw_count = 0
            for line in all_lines:
                if re.match(r"O*-O*$", line):
                    count_win += 1
                    break
                if "O" in line and "X" in line:
                    draw_count += 1
            if draw_count == 8:
                count_draw += 1
            self.board[y][x] = "-"
        if count_win == len(l_brank):
            print("You will have to be win.")
            return True
        if count_draw == len(l_brank):
            print("You will have to be draw.")
            return True
        print("No answer.")
        return True

    def find_brank(self):
        l_brank = []
        for y, row in enumerate(self.board):
            for x, ele in enumerate(row):
                if ele == "-":
                    l_brank.append((x, y))
        return l_brank

    def print_board(self):
        print("1 {}\n2 {}\n3 {}\n  ABC".format("".join(self.board[0]), "".join(self.board[1]), "".join(self.board[2])))
        return True


def question_5():
    game = Game()
    game.start()


if __name__ == "__main__":
    question_5()
