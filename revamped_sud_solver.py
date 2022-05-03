from typing import List
from Stack import Stack
import numpy as np


class Sudoku:
    def __init__(self, matrix):
        self.board = np.array(matrix)
        self.numbers = Stack()
        self.numbers_indices = Stack()

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

    def _check_valid(self, indices: List, number: int):
        # Check in column
        row, column = indices
        for i in range(0, 82, 9):
            if number in self.board.flatten()[i:i+column+1]:
                return True

        # Check in row
        if number in self.board[row]:
            return True

        # Check in grid
        grid = []
        range_of_i, range_of_j = self._generate_grid(row, column)
        for i in range_of_i:
            for j in range_of_j:
                grid.append(self.board[i][j])
        if number in grid:
            return True
        return False

    def _generate_grid(self, i, j):
        range_of_i, range_of_j = [], []
        if i % 3 == 0:
            range_of_i = [i, i+1, i+2]
        if i % 3 == 1:
            range_of_i = [i-1, i, i+1]
        if i % 3 == 2:
            range_of_i = [i-2, i-1, i]
        if j % 3 == 0:
            range_of_j = [j, j+1, j+2]
        if j % 3 == 1:
            range_of_j = [j-1, j, j+1]
        if j % 3 == 2:
            range_of_j = [j-2, j-1, i]
        return range_of_i, range_of_j


def main():
    sud = Sudoku([[7, 8, 0, 4, 0, 0, 1, 2, 0], [6, 0, 0, 0, 7, 5, 0, 0, 9], [0, 0, 0, 6, 0, 1, 0, 7, 8], [0, 0, 7, 0, 4, 0, 2, 6, 0], [
        0, 0, 1, 0, 5, 0, 9, 3, 0], [9, 0, 4, 0, 6, 0, 0, 0, 5], [0, 7, 0, 3, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 7, 4, 0, 0], [0, 4, 9, 2, 0, 6, 0, 0, 7]])
    sud = Sudoku(np.zeros((9, 9), dtype=int))
    sud.print_board()
    print(sud._check_valid([1, 1], 7))


if __name__ == '__main__':
    main()
