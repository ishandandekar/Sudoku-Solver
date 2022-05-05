from Stack import Stack
import numpy as np


class Sudoku:

    # def _check_valid(self, indices: List, number: int):  # DO NOT USE THIS
    #     # Check in column
    #     row, column = indices
    #     for i in range(0, 82, 9):
    #         if number in self.board.flatten()[i:i+column+1]:
    #             return True

    #     # Check in row
    #     if number in self.board[row]:
    #         return True

    #     # Check in grid
    #     grid = []
    #     range_of_i, range_of_j = self._generate_grid(row, column)
    #     for i in range_of_i:
    #         for j in range_of_j:
    #             grid.append(self.board[i][j])
    #     if number in grid:
    #         return True
    #     return False

    # i is row index (starts with 0), j is column index (starts with 0)
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

    def solve(self):
        pass

    def _grid_creator(self, i, j):
        if i % 3 == 0:
            range_of_i = [i, i+1, i+2]
            grid_row_index = 0
        if i % 3 == 1:
            range_of_i = [i-1, i, i+1]
            grid_row_index = 1
        if i % 3 == 2:
            range_of_i = [i-2, i-1, i]
            grid_row_index = 2
        if j % 3 == 0:
            range_of_j = [j, j+1, j+2]
            grid_col_index = 0
        if j % 3 == 1:
            range_of_j = [j-1, j, j+1]
            grid_col_index = 1
        if j % 3 == 2:
            range_of_j = [j-2, j-1, i]
            grid_col_index = 2
        return range_of_i, range_of_j, [grid_row_index, grid_col_index]

    # THIS IS THE CORRECT VALIDATOR FOR NUMBERS TO BE INSERTED IN THE SUDOKU
    def _check_valid(self, indices: list, number: int) -> bool:
        row, column = indices
        # To check in column
        col_array = []
        for i in self.board:
            col_array.append(i[column])
        if number in col_array:
            print(f"{number} is there in column {column}")
            return True

        # To check in row
        for i in range(len(self.board)):
            row_arr = self.board[i]
            if i == row and number in row_arr:
                print(f"{number} is there in row {i}")
                return True
        range_of_row, range_of_column, grid_indices = self._grid_creator(
            row, column)
        grid_arr = []
        for i in range_of_row:
            for j in range_of_column:
                grid_arr.append(self.board[i][j])

        if number in grid_arr:
            print(f"{number} is there in grid {grid_indices}")
            return True
        return False


def main():
    sud = Sudoku([[7, 8, 0, 4, 0, 0, 1, 2, 0], [6, 0, 0, 0, 7, 5, 0, 0, 9], [0, 0, 0, 6, 0, 1, 0, 7, 8], [0, 0, 7, 0, 4, 0, 2, 6, 0], [
        0, 0, 1, 0, 5, 0, 9, 3, 0], [9, 0, 4, 0, 6, 0, 0, 0, 5], [0, 7, 0, 3, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 7, 4, 0, 0], [0, 4, 9, 2, 0, 6, 0, 0, 7]])
    sud.print_board()
    print(sud._check_valid([0, 0], 7))


if __name__ == '__main__':
    main()
