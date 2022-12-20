from re import S
import tkinter
from tkinter import filedialog

filename = filedialog.askopenfilename(
    initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
counter = 0
with open(filename) as f:
    for line in f.readlines():
        ranges = line.split(',')
        first_range = ranges[0].split('-')
        second_range = ranges[1].split('-')
        first_range = [int(first_range[0]), int(first_range[1])]
        second_range = [int(second_range[0]), int(second_range[1])]
        if first_range[0] <= second_range[0] and first_range[1] >= second_range[1] or first_range[0] >= second_range[0] and first_range[1] <= second_range[1]:
            counter += 1
print(counter)
