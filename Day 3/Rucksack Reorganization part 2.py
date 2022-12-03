from re import S
import tkinter
from tkinter import filedialog

filename = filedialog.askopenfilename(
    initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
sum = 0
with open(filename) as f:
    first = []
    second = []
    third = []
    i = 0
    for line in f.readlines():
        if i % 3 == 0:
            first = line
        if i % 3 == 1:
            second = line
        if i % 3 == 2:
            third = line
            for ch in first:
                if ch in second and ch in third:
                    ascii_val = ord(ch)
                    cur = 0
                    if ascii_val > 95:
                        cur = ascii_val - 96
                    else:
                        cur = ascii_val - 64 + 26
                    sum += cur
                    break
        i += 1
print(sum)
