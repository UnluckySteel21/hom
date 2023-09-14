import tkinter as tk
import random

class car():
    def __init__(self):
        self.brand = "Mašīnas marka"
        self.model = "Mašīnas modelis"
        self.PhoneNumber = "Telefona numurs"
        self.WinNumber = "Win numurs"
        self.Date = "Datums"
        self.description = "Apraksts"
        self.id = "id"
    
def changePar():
    entries.append(b)

def Onload():
    global entries, b
    entries = []
    root = tk.Tk()
    height = 1
    width = 7
    displayFrame = tk.Frame(root, border=10)
    displayFrame.pack()
    for i in range(height):
        for j in range(width):
            b = tk.Entry(displayFrame)
            b.grid(row=i, column=j)
    button = tk.Button(displayFrame, function=changePar())
    button.grid(column= j+1, row=i+1)
    
    root.mainloop()
Onload()
for entry in entries:
    print(entry.get())
