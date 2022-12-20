from re import S
import tkinter
from tkinter import filedialog

filename = filedialog.askopenfilename(
    initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
counter = 0
line = ""
with open(filename) as f:
    line = f.readlines()
    for idx in range(len(line[0])):
        st = line[0][idx:int(idx+14)]
        flag = True
        for char in st:
            if st.count(char) != 1:
                flag = False
                break
        if flag:
            counter = idx+14
            break
print(counter)
