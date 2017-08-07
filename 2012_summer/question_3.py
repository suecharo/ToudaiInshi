# coding: utf-8
import sys
import time
import os
import termios


class Game(object):
    def __init__(self):
        self.board = [[None] * 9 for __ in range(15)] # board[y][x]
        self.ball_bool = False
        self.ball_pos = [None, None] # [x, y]
        self.ball_state = 0 # 0 : right, 1 : left
        self.key_input = None
        self.score = 0
        self.bullet_1 = False
        self.bullet_1_pos = [None, None] # [x, y]
        self.can_move_bullet_1 = False
        self.bullet_2 = False
        self.bullet_2_pos = [None, None] # [x, y]
        self.can_move_bullet_2 = False

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

    def change_key_mode(self):
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] &= ~termios.ICANON
        new[3] &= ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, new)
        return True

    def get_key(self):
        if self.key_input == "i":
            if self.bullet_1 is False:
                self.appear_bullet(1)
            else:
                if self.bullet_2 is False:
                    self.appear_bullet(2)
        self.key_input = None
        return True

    def appear_bullet(self, bullet_num):
        if bullet_num == 1:
            self.bullet_1 = True
            self.bullet_1_pos = [4, 13] # [x, y]
            self.board[self.bullet_1_pos[1]][self.bullet_1_pos[0]] = "e"
            self.can_move_bullet_1 = False
        elif bullet_num == 2:
            self.bullet_2 = True
            self.bullet_2_pos = [4, 13] # [x, y]
            self.board[self.bullet_2_pos[1]][self.bullet_2_pos[0]] = "e"
            self.can_move_bullet_2 = False
        return True

    def about_ball(self):
        if self.ball_bool is False:
            self.appear_ball()
        else:
            self.move_ball()

    def about_bullet(self):
        if self.bullet_1 is True:
            if self.can_move_bullet_1 is True:
                self.move_bullet(1)
            else:
                self.can_move_bullet_1 = True

        if self.bullet_2 is True:
            if self.can_move_bullet_2 is True:
                self.move_bullet(2)
            else:
                self.can_move_bullet_2 = True

    def move_bullet(self, bullet_num):
        if bullet_num == 1:
            if self.bullet_1_pos[1] == 1:
                if self.bullet_1_pos[0] == 0 or self.bullet_1_pos[0] == 8
                    self.board[self.bullet_1_pos[1]][self.bullet_1_pos[0]] = "|"
                    self.bullet_1_pos[1] -= 1
                else:
                    self.board[self.bullet_1_pos[1]][self.bullet_1_pos[0]] = " "
                    self.bullet_1_pos[1] -= 1
            elif self.bullet_1_pos[1] == 0:
                self.bullet_1 = False
                self.bullet_1_pos = [None, None]
                self.can_move_bullet_1 = False
            else:
                if self.bullet_1_pos[0] == 0 or self.bullet_1_pos[0] == 8
                    self.board[self.bullet_1_pos[1]][self.bullet_1_pos[0]] = "|"
                else:
                    self.board[self.bullet_1_pos[1]][self.bullet_1_pos[0]] = " "
                self.bullet_1_pos[1] -= 1
                self.board[self.bullet_1_pos[1]][self.bullet_1_pos[0]] = "e"
        elif bullet_num == 2:
            if self.bullet_2_pos[1] == 1:
                if self.bullet_2_pos[0] == 0 or self.bullet_2_pos[0] == 8
                    self.board[self.bullet_2_pos[1]][self.bullet_2_pos[0]] = "|"
                    self.bullet_2_pos[1] -= 1
                else:
                    self.board[self.bullet_2_pos[1]][self.bullet_2_pos[0]] = " "
                    self.bullet_2_pos[1] -= 1
            elif self.bullet_2_pos[1] == 0:
                self.bullet_2 = False
                self.bullet_2_pos = [None, None]
                self.can_move_bullet_2 = False
            else:
                if self.bullet_2_pos[0] == 0 or self.bullet_2_pos[0] == 8
                    self.board[self.bullet_2_pos[1]][self.bullet_2_pos[0]] = "|"
                else:
                    self.board[self.bullet_2_pos[1]][self.bullet_2_pos[0]] = " "
                self.bullet_2_pos[1] -= 1
                self.board[self.bullet_2_pos[1]][self.bullet_2_pos[0]] = "e"
        return True

    def collision(self):
        if self.bullet_1 is True:
            if self.ball_pos[0] == self.bullet_1_pos[0] and self.ball_pos[1] == self.bullet_2[1]:
                self.board[self.ball_pos[1]][self.ball_pos[0]] = " "
                self.ball_bool = False
                self.ball_pos = [None, None]
                self.ball_state = 0
                self.bullet_1 = False
                self.bullet_1_pos = [None, None]
                self.can_move_bullet_1 = False
        elif self.bullet_2 is True:
            if self.ball_pos[0] == self.bullet_2_pos[0] and self.ball_pos[1] == self.bullet_2[1]:
                self.board[self.ball_pos[1]][self.ball_pos[0]] = " "
                self.ball_bool = False
                self.ball_pos = [None, None]
                self.ball_state = 0
                self.bullet_2 = False
                self.bullet_2_pos = [None, None]
                self.can_move_bullet_2 = False

    def play(self):
        self.make_first_board()
        self.change_key_mode()
        self.display_board()
        self.key_input = sys.stdin.read()
        time.sleep(0.5)

        while True:
            if self.key_input is not None:
                self.get_key()
            self.about_bullet()
            self.about_ball()
            self.collision()
            self.display_board()
            self.key_input = sys.stdin.read()
            time.sleep(0.5)


def question_3():
    game = Game()
    game.play()


if __name__ == "__main__":
    question_3()
