from re import S
import tkinter
from tkinter import filedialog

filename = filedialog.askopenfilename(
    initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
sum = 0
with open(filename) as f:
    for line in f.readlines():
        mid = int(len(line)/2)
        first = line[0:mid]
        second = line[mid:-1]
        for ch in first:
            if ch in second:
                ascii_val = ord(ch)
                cur = 0
                if ascii_val > 95:
                    cur = ascii_val - 96
                else:
                    cur = ascii_val - 64 + 26
                print(first + "           " + second)
                print(cur)
                sum += cur
                break
print(sum)
