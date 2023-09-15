#importing things i need for the project
import tkinter as tk
import random


#car class that is somewhat a default spreadsheet
class car():
    def __init__(self, brand, model, phoneNumber, winNumber, date, description, identification, licensePlate):
        self.brand = brand
        self.model = model
        self.phoneNumber = phoneNumber
        self.winNumber = winNumber
        self.date = date
        self.description = description
        self.identification = identification
        self.licensePlate = licensePlate
    
    def changePar():
        pass

#the main function of the programm that displays the start of the programm
def Onload():
    root = tk.Tk()

    #the input frame. Deals with new input + the description about what to write where
    inputFrame = tk.Frame(root, border=10)
    inputFrame.pack()
    identificationLabel = tk.Label(inputFrame, text="Identifikācija")
    identificationLabel.grid(column=1, row=1)
    dateLabel = tk.Label(inputFrame, text="Datums un laiks")
    dateLabel.grid(column=2, row=1)
    brandLabel = tk.Label(inputFrame, text="Marka")
    brandLabel.grid(column=3, row=1)
    modelLabel = tk.Label(inputFrame, text="Modelis")
    modelLabel.grid(column=4, row=1)
    phoneNumberLabel = tk.Label(inputFrame, text="Telefona numurs")
    phoneNumberLabel.grid(column=5, row=1)
    winNumberLabel = tk.Label(inputFrame, text="Mašīnas win numurs")
    winNumberLabel.grid(column=6, row=1)
    licensePlateLabel = tk.Label(inputFrame, text="Mašīnas numurzīme")
    licensePlateLabel.grid(column=7, row=1)
    descriptionLabel = tk.Label(inputFrame, text="Apraksts")
    descriptionLabel.grid(column=8, row=1)
    
    root.mainloop()

Onload()