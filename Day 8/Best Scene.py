from re import S
import tkinter
from tkinter import filedialog


def scene_point_dfs(i, j, matrix):
    up = 0
    down = 0
    left = 0
    right = 0
    v = 1
    while i+v < len(matrix)-1 and matrix[i][j] > matrix[i+v][j]:
        v += 1
    down = v
    v = 1
    while i-v > 0 and matrix[i][j] > matrix[i-v][j]:
        v += 1
    up = v
    v = 1
    while j+v < len(matrix[0])-1 and matrix[i][j] > matrix[i][j+v]:
        v += 1
    right = v
    v = 1
    while j-v > 0 and matrix[i][j] > matrix[i][j-v]:
        v += 1
    left = v
    v = 1
    output = up*down*right*left
    return output


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
scene_points = 0
matrix = matrix[0]
for i in range(len(matrix)-2):
    for j in range(len(matrix[0])-2):
        scene_points = max(scene_point_dfs(i+1, j+1, matrix), scene_points)
print(scene_points)
