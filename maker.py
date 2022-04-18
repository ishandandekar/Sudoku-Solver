import numpy as np
import random


class sudoku_gen:
    def __init__(self) -> None:
        self.mat = [[3, 0, 6, 5, 0, 8, 4, 0, 0], [5, 2, 0, 0, 0, 0, 0, 0, 0], [8, 7, 0, 0, 0, 0, 3, 1],
                    [0, 0, 3, 0, 1, 0, 0, 8, 0], [9, 0, 0, 8, 6, 3, 0, 0, 5], [0, 5, 0, 0, 9, 0, 6, 0, 0], [1, 3, 0, 0, 0, 0, 2, 5, 0], [0, 0, 0, 0, 0, 0, 0, 7, 4], [0, 0, 5, 2, 0, 6, 3, 0, 0]]
        self.lst = range(1, 10, 1)
        self.path = []
        self.path_indices = [[]]

    @property
    def is_empty(self):
        count = 0
        for i in self.mat:
            for j in i:
                if j == 0:
                    count += 1
        return count

    def traverse(self):
        for i in range(len(self.mat)):
            temp = self.lst
            for j in range(len(i)):
                if self.mat[i][j] != 0:
                    pass

    def check(self, i, j, number):
        # to check in row i
        for k in range(0, 82, 9):
            if k == i:
                if number in self.mat.flatten()[i:i+10]:
                    return True

        # to check in column j
        col_lst = []
        for i in self.mat:
            col_lst.append(i[j])
        if number in col_lst:
            return True

        grid_lst = []
        # to get the grid with ith row and jth column
        if i % 3 == 0:
            range_of_i = [i, i+1, i+2]
        if i % 3 == 1:
            range_of_i = [i-1, i, i+1]
        if i % 3 == 2:
            range_of_i = [i-2, i-1, i]
        if j % 3 == 0:
            range_of_j = [j, j+1, j+2]
        if j % 3 == 1:
            range_of_i = [j-1, j, j+1]
        if j % 3 == 2:
            range_of_i = [j-2, j-1, i]

        for k in range_of_i:
            row_lst = self.mat[k]
            grid_lst.append(
                [x for x in row_lst if row_lst.index(x) in range_of_j])

    def update_board(self, i, j, number):
        self.mat[i][j] = number


obj = sudoku_gen()
print(obj.is_empty)
