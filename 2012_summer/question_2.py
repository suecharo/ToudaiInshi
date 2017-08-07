# coding: utf-8
import sys
import time
import os


class Game(object):
    def __init__(self):
        self.board = [[None] * 9 for __ in range(15)] # board[y][x]
        self.ball_bool = False
        self.ball_pos = [None, None] # [x, y]
        self.ball_state = 0 # 0 : right, 1 : left

    def make_first_board(self):
        for y in range(15):
            for x in range(9):
                if x == 0 or x == 8:
                    self.board[y][x] = "|"
                else:
                    if y == 0:
                        if x == 4:
                            self.board[y][x] = "V"
                        else:
                            self.board[y][x] = "-"
                    elif y == 14:
                        if x == 4:
                            self.board[y][x] = "X"
                        else:
                            self.board[y][x] = "."
                    else:
                        self.board[y][x] = " "
        return True

    def display_board(self):
        board_str = "\n".join(["".join(row) for row in self.board])
        os.system("clear")
        print(board_str)
        return True

    def appear_ball(self):
        self.ball_bool = True
        self.ball_pos = [5, 1]
        self.board[self.ball_pos[1]][self.ball_pos[0]] = "o"
        return True

    def move_ball(self):
        if self.ball_pos[1] == 13:
            if self.ball_pos[0] == 0 or self.ball_pos[0] == 8:
                self.board[self.ball_pos[1]][self.ball_pos[0]] = "|"
            else:
                self.board[self.ball_pos[1]][self.ball_pos[0]] = " "
            self.ball_pos[1] += 1
        elif self.ball_pos[1] == 14:
            self.ball_bool = False
            self.ball_pos = [None, None]
            self.ball_state = 0
        else:
            if self.ball_state == 0:
                if self.ball_pos[0] == 8:
                    self.board[self.ball_pos[1]][self.ball_pos[0]] = "|"
                    self.ball_state = 1
                    self.ball_pos[0] = 7
                    self.ball_pos[1] += 1
                else:
                    self.board[self.ball_pos[1]][self.ball_pos[0]] = " "
                    self.ball_pos[0] += 1
                    self.ball_pos[1] += 1
            elif self.ball_state == 1:
                if self.ball_pos[0] == 0:
                    self.board[self.ball_pos[1]][self.ball_pos[0]] = "|"
                    self.ball_state = 0
                    self.ball_pos[0] = 1
                    self.ball_pos[1] += 1
                else:
                    self.board[self.ball_pos[1]][self.ball_pos[0]] = " "
                    self.ball_pos[0] -= 1
                    self.ball_pos[1] += 1
            self.board[self.ball_pos[1]][self.ball_pos[0]] = "o"
        return True

    def play(self):
        self.make_first_board()
        self.display_board()
        time.sleep(0.5)
        while True:
            if self.ball_bool is False:
                self.appear_ball()
            else:
                self.move_ball()
            self.display_board()
            time.sleep(0.5)


def question_2():
    game = Game()
    game.play()


if __name__ == "__main__":
    question_2()
