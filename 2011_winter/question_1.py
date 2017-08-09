# coding: utf-8
class Board():
    def __init__(self):
        self.board = [["-"] * 3 for __ in range(3)] # [y][x]

    def input_as_line(self, line):
        for x in range(3):
            for y in range(3):
                self.board[y][x] = line[x + y * 3]

    def print_board(self):
        print("\n".join(["".join(row) for row in self.board]))


def question_1():
    for i in range(4):
        board = Board()
        if i == 0:
            board.input_as_line("OX-OXXOO-")
        elif i == 1:
            board.input_as_line("XXOOOO-X-")
        elif i == 2:
            board.input_as_line("XXOOX-OOX")
        elif i == 3:
            board.input_as_line("XOXXOOOXO")
        board.print_board()
        if i != 3:
            print("-" * 40)


if __name__ == "__main__":
    question_1()
