import tkinter as tk
import random

class car():
    def __init__(self):
        self.brand = "Mašīnas marka"
        self.model = "Mašīnas modelis"
        self.phoneNumber = "Telefona numurs"
        self.winNumber = "Win numurs"
        self.date = "Datums"
        self.description = "Apraksts"
        self.id = "id"
        self.licensePlate = ""
    
    def changePar():
        pass

def Onload():
    root = tk.Tk()
    displayFrame = tk.Frame(root, border=10)
    displayFrame.pack()
    root.mainloop()