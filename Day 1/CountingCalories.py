import tkinter
from tkinter import filedialog

filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
calories_per_elf = []
elf_calories = 0
with open(filename) as f:
    for line in f.readlines():
        if line == '\n':
            calories_per_elf.append(elf_calories)
            elf_calories = 0
        else:
            elf_calories += int(line)
calories_per_elf.sort()
print(calories_per_elf[-1] + calories_per_elf[-2] + calories_per_elf[-3])