#importing things i need for the project
import tkinter as tk
import random


#car class that is somewhat a default spreadsheet
class car():
    def __init__(self, identificationEntry, dateEntry, brandEntry, modelEntry, phoneNumberEntry, winNumberEntry, licensePlateEntry, descriptionEntry):
        self.identification = identificationEntry
        self.date = dateEntry
        self.brand = brandEntry
        self.model = modelEntry
        self.phoneNumber = phoneNumberEntry
        self.winNumber = winNumberEntry
        self.licensePlate = licensePlateEntry
        self.description = descriptionEntry
        

#the main function of the programm that displays the start of the programm
def Onload():
    root = tk.Tk()
    global identificationEntry, dateEntry, brandEntry, modelEntry, phoneNumberEntry, winNumberEntry, licensePlateEntry, descriptionEntry
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

    #text input
    identificationEntry = tk.Entry(inputFrame, text="Identifikācija")
    identificationEntry.grid(column=1, row=2)
    dateEntry = tk.Entry(inputFrame, text="Datums un laiks")
    dateEntry.grid(column=2, row=2)
    brandEntry = tk.Entry(inputFrame, text="Marka")
    brandEntry.grid(column=3, row=2)
    modelEntry = tk.Entry(inputFrame, text="Modelis")
    modelEntry.grid(column=4, row=2)
    phoneNumberEntry = tk.Entry(inputFrame, text="Telefona numurs")
    phoneNumberEntry.grid(column=5, row=2)
    winNumberEntry = tk.Entry(inputFrame, text="Mašīnas win numurs")
    winNumberEntry.grid(column=6, row=2)
    licensePlateEntry = tk.Entry(inputFrame, text="Mašīnas numurzīme")
    licensePlateEntry.grid(column=7, row=2)
    descriptionEntry= tk.Entry(inputFrame, text="Apraksts")
    descriptionEntry.grid(column=8, row=2)
    #input button
    inputButton = tk.Button(inputFrame, text="Iesniegt klienta datus", command=dataInput)
    inputButton. grid(column=4, columnspan=2, row=3)

    root.mainloop()

def dataInput():
    NewCar = car(identificationEntry.get(), dateEntry.get(), brandEntry.get(), modelEntry.get(), phoneNumberEntry.get(), winNumberEntry.get(), licensePlateEntry.get(), descriptionEntry.get())
    print(NewCar.__dict__)

Onload()