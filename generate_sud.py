import numpy as np
import random

mat = np.zeros((9, 9))
mat[1][1] = 1
mat[2][2] = 1
mat[1][0] = 3
print(mat)
# for i in mat:
#     for j in i:
#         if j == 1:
#             print(f"{i} , {j} = 1")
arr = mat.flatten()
# for i in range(len(arr)):
#     if arr[i] == 1:
#         print(i)

numb = 1
for i in range(0, 82, 9):
    if numb in mat.flatten()[i:i+10]:
        print("there")

# checking in column 0
temp = []
for i in mat:
    temp.append(i[0])
temp = np.array(temp)
print(temp)

# grid 0

grid_0 = []
for i in mat[:3]:
    grid_0.append(i[:3])
grid_0 = np.array(grid_0)
print(grid_0)


# to determine grid
def check(i, j, number):  # i is row index (starts with 0), j is column index (starts with 0)
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
