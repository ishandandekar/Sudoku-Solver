import numpy as np
import random

from pyparsing import col

# mat = np.zeros((9, 9))
# mat[1][1] = 1
# mat[2][2] = 1
# mat[1][0] = 3
# print(mat)
# # for i in mat:
# #     for j in i:
# #         if j == 1:
# #             print(f"{i} , {j} = 1")
# arr = mat.flatten()
# # for i in range(len(arr)):
# #     if arr[i] == 1:
# #         print(i)

# numb = 1
# for i in range(0, 82, 9):
#     if numb in mat.flatten()[i:i+10]:
#         print("there")

# # checking in column 0
# temp = []
# for i in mat:
#     temp.append(i[0])
# temp = np.array(temp)
# print(temp)

# # grid 0

# grid_0 = []
# for i in mat[:3]:
#     grid_0.append(i[:3])
# grid_0 = np.array(grid_0)
# print(grid_0)
# to determine grid


def check(i, j):  # i is row index (starts with 0), j is column index (starts with 0)
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


def _helper_check(indices: list, number: int, board: list):
    row, column = indices
    # To check in column
    col_array = []
    for i in board:
        col_array.append(i[column])
    if number in col_array:
        print(f"{number} is there in column {column}")

    # To check in row
    for i in range(len(board)):
        row_arr = board[i]
        if i == row and number in row_arr:
            print(f"{number} is there in row {i}")
    range_of_row, range_of_column, grid_indices = check(row, column)
    grid_arr = []
    for i in range_of_row:
        for j in range_of_column:
            grid_arr.append(board[i][j])

    if number in grid_arr:
        print(f"{number} is there in grid {grid_indices}")


board = [[7, 8, 0, 4, 0, 0, 1, 2, 0], [6, 0, 0, 0, 7, 5, 0, 0, 9], [0, 0, 0, 6, 0, 1, 0, 7, 8], [0, 0, 7, 0, 4, 0, 2, 6, 0], [
    0, 0, 1, 0, 5, 0, 9, 3, 0], [9, 0, 4, 0, 6, 0, 0, 0, 5], [0, 7, 0, 3, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 7, 4, 0, 0], [0, 4, 9, 2, 0, 6, 0, 0, 7]]
_helper_check([1, 4], 7, board=board)
