# coding: utf-8
import re
import random
import time

class Game():
    def __init__(self):
        self.board = [["-"] * 3 for __ in range(3)] # [y][x]
        self.count = 0

    def start(self):
        print("*" * 3 + " GAME START!! " + "*" * 3)
        self.print_board()
        while True:
            time.sleep(1)
            input_x, input_y = self.get_input_from_computer()
            self.input_board(input_x, input_y)
            all_lines = self.make_all_lines()
            if self.check_win(all_lines):
                print("*" * 40)
                self.print_board()
                if self.count % 2 == 0:
                    print("Computer_O win!!")
                else:
                    print("Computer_X win!!")
                break
            self.count += 1
            if self.count == 9:
                print("*" * 40)
                self.print_board()
                print("Draw.")
                break
            print("-" * 40)
            self.print_board()

    def get_input_from_computer(self):
        l_brank = []
        for y, row in enumerate(self.board):
            for x, ele in enumerate(row):
                if ele == "-":
                    l_brank.append((x, y))
        input_x, input_y = random.choice(l_brank)
        if self.count % 2 == 0:
            print("Computer_O : " + str(input_y + 1) + "ABC"[input_x])
        else:
            print("Computer_X : " + str(input_y + 1) + "ABC"[input_x])
        return input_x, input_y

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

    def print_board(self):
        print("1 {}\n2 {}\n3 {}\n  ABC".format("".join(self.board[0]), "".join(self.board[1]), "".join(self.board[2])))
        return True


def question_4():
    game = Game()
    game.start()


if __name__ == "__main__":
    question_4()
