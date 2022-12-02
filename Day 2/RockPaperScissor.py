import tkinter
from tkinter import filedialog


def scoring(p1, p2):
    if p1 == "A" and p2 == "X" or p1 == "B" and p2 == "Y" or p1 == "C" and p2 == "Z":
        return 3
    if p1 == "A" and p2 == "Y" or p1 == "B" and p2 == "Z" or p1 == "C" and p2 == "X":
        return 6
    if p1 == "A" and p2 == "Z" or p1 == "B" and p2 == "X" or p1 == "C" and p2 == "Y":
        return 0


dict1 = {"X": 1, "Y": 2, "Z": 3}
total = 0
filename = filedialog.askopenfilename(
    initialdir="/",
    title="Select a File",
    filetypes=(("Text files", "*.txt*"), ("all files", "*.*")),
)
with open(filename) as f:
    for line in f.readlines():
        total += dict1[line[2]] + scoring(line[0], line[2])
print(total)
