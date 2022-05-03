from Stack import Stack
import numpy as np


class Sudoku:
    def __init__(self, matrix):
        self.board = matrix

    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("------------------------")
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")


def main():
    sud = Sudoku([[7, 8, 0, 4, 0, 0, 1, 2, 0], [6, 0, 0, 0, 7, 5, 0, 0, 9], [0, 0, 0, 6, 0, 1, 0, 7, 8], [0, 0, 7, 0, 4, 0, 2, 6, 0], [
        0, 0, 1, 0, 5, 0, 9, 3, 0], [9, 0, 4, 0, 6, 0, 0, 0, 5], [0, 7, 0, 3, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 7, 4, 0, 0], [0, 4, 9, 2, 0, 6, 0, 0, 7]])
    sud = Sudoku(np.zeros((9, 9), dtype=int))
    sud.print_board()


if __name__ == '__main__':
    main()
