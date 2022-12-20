from re import S
import tkinter
from tkinter import filedialog

filename = filedialog.askopenfilename(
    initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
counter = 0
matrix = []
with open(filename) as f:
    matrix.append(f.readlines())
for i in range(len(matrix[0])):
    line = matrix[0][i]
    matrix[0][i] = [int(line[j:j+1])
                    for j in range(0, len(line), 1) if line[j:j+1].isnumeric()]
# two strats, strat 1 use recursion (leetcode island mapping style), strat 2(just scan both ways O(n^2))
coordinates = set()
matrix = matrix[0]
for i in range(len(matrix)):
    max_forward = -1
    max_backward = -1
    for j in range(len(matrix[0])):
        if max_forward < matrix[i][j]:
            max_forward = matrix[i][j]
            coordinates.add(tuple([i, j]))
        if max_backward < matrix[i][len(matrix[0]) - 1 - j]:
            max_backward = matrix[i][len(matrix[0]) - 1 - j]
            coordinates.add(tuple([i, len(matrix[0]) - 1 - j]))
for j in range(len(matrix[0])):
    max_up = -1
    max_down = -1
    for i in range(len(matrix)):
        if max_up < matrix[i][j]:
            max_up = matrix[i][j]
            coordinates.add(tuple([i, j]))
        if max_down < matrix[len(matrix) - 1 - i][j]:
            max_down = matrix[len(matrix) - 1 - i][j]
            coordinates.add(tuple([len(matrix) - 1 - i, j]))
print(len(coordinates))
