import tkinter
from tkinter import filedialog


def rps(p1, outcome):
    if (
        p1 == "A"
        and outcome == "Y"
        or p1 == "C"
        and outcome == "Z"
        or p1 == "B"
        and outcome == "X"
    ):
        return 1
    if (
        p1 == "B"
        and outcome == "Y"
        or p1 == "A"
        and outcome == "Z"
        or p1 == "C"
        and outcome == "X"
    ):
        return 2
    if (
        p1 == "C"
        and outcome == "Y"
        or p1 == "B"
        and outcome == "Z"
        or p1 == "A"
        and outcome == "X"
    ):
        return 3


dict_outcome = {"X": 0, "Y": 3, "Z": 6}
total = 0
filename = filedialog.askopenfilename(
    initialdir="/",
    title="Select a File",
    filetypes=(("Text files", "*.txt*"), ("all files", "*.*")),
)
with open(filename) as f:
    for line in f.readlines():
        t = dict_outcome[line[2]]
        total += t + rps(line[0], line[2])
print(total)
