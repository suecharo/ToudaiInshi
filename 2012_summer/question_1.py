# coding: utf-8
class Game(object):
    def __init__(self):
        self.board = [[None] * 9 for __ in range(15)] # board[y][x]

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
        for row in self.board:
            print("".join(row))
        return True


def question_1():
    game = Game()
    game.make_first_board()
    game.display_board()


if __name__ == "__main__":
    question_1()
