#importing things i need for the project
import tkinter as tk
import random
from datetime import datetime

#car class that is somewhat a default spreadsheet
class Car():
    def __init__(self, identificationNumber, formated_now, brandEntry, modelEntry, phoneNumberEntry, winNumberEntry, licensePlateEntry, descriptionEntry):
        self.identification = identificationNumber
        self.date = formated_now
        self.brand = brandEntry
        self.model = modelEntry
        self.phoneNumber = phoneNumberEntry
        self.winNumber = winNumberEntry
        self.licensePlate = licensePlateEntry
        self.description = descriptionEntry


def allCLients():
    ...

def pendingClients():
    ...

def back():
    inputFrame.destroy()
    mainLog()

#the main function of the programm that displays the start of the programm
def mainLog():
    global mainFrame
    mainFrame = tk.Frame(root)
    mainFrame.pack()
    newClientButton = tk.Button(mainFrame, text="Jauns klients", command=newClient, font=("Calibri", 30), relief="groove", width=20, )
    newClientButton.pack(anchor="center", pady=75)
    pendingClientsButton = tk.Button(mainFrame, text = "Uzgaidāmā telpa", command=pendingClients, font=("Calibri", 30), width=20, relief="groove")
    pendingClientsButton.pack(anchor="center", pady=75)
    viewAllClientsButton = tk.Button(mainFrame, text="Remontdarbu vēsture", command=allCLients, font=("Calibri", 30), width=20, relief="groove")
    viewAllClientsButton.pack(anchor="center", pady=75)


#the tkinter window for client info input
def newClient():
    global inputFrame, identificationNumber, formated_now, brandEntry, modelEntry, phoneNumberEntry, winNumberEntry, licensePlateEntry, descriptionEntry
    #the input frame. Deals with new input + the description about what to write where
    mainFrame.destroy()
    identificationNumber = ''.join(random.choice('0123456789') for _ in range(9))
    now = datetime.now()
    formated_now = now.strftime("%Y-%m-%d %H:%M:%S")

    inputFrame = tk.Frame(root, border=10)
    inputFrame.pack()
    homeButton = tk.Button(inputFrame, text=" ↰ \n Uz sākuma ekrānu", command=back, font=("Calibri", 12), relief="groove")
    homeButton.grid(column=1, row=1, pady=20)
    identificationLabel = tk.Label(inputFrame, text="Identifikācija", font=("Calibri", 12))
    identificationLabel.grid(column=1, row=2)
    dateLabel = tk.Label(inputFrame, text="Datums un laiks", font=("Calibri", 12))
    dateLabel.grid(column=2, row=2)
    brandLabel = tk.Label(inputFrame, text="Marka", font=("Calibri", 12))
    brandLabel.grid(column=3, row=2)
    modelLabel = tk.Label(inputFrame, text="Modelis", font=("Calibri", 12))
    modelLabel.grid(column=4, row=2)
    phoneNumberLabel = tk.Label(inputFrame, text="Telefona numurs", font=("Calibri", 12))
    phoneNumberLabel.grid(column=5, row=2)
    winNumberLabel = tk.Label(inputFrame, text="Mašīnas win numurs", font=("Calibri", 12))
    winNumberLabel.grid(column=6, row=2)
    licensePlateLabel = tk.Label(inputFrame, text="Mašīnas numurzīme", font=("Calibri", 12))
    licensePlateLabel.grid(column=7, row=2)
    descriptionLabel = tk.Label(inputFrame, text="Apraksts", font=("Calibri", 12))
    descriptionLabel.grid(column=8, row=2)

    #text input
    identificationEntry = tk.Label(inputFrame, text=identificationNumber, font=("Calibri", 12))
    identificationEntry.grid(column=1, row=3)
    dateEntry = tk.Label(inputFrame, text=formated_now, font=("Calibri", 12))
    dateEntry.grid(column=2, row=3)
    brandEntry = tk.Entry(inputFrame, text="Marka", font=("Calibri", 12))
    brandEntry.grid(column=3, row=3)
    modelEntry = tk.Entry(inputFrame, text="Modelis", font=("Calibri", 12))
    modelEntry.grid(column=4, row=3)
    phoneNumberEntry = tk.Entry(inputFrame, text="Telefona numurs", font=("Calibri", 12))
    phoneNumberEntry.grid(column=5, row=3)
    winNumberEntry = tk.Entry(inputFrame, text="Mašīnas win numurs", font=("Calibri", 12))
    winNumberEntry.grid(column=6, row=3)
    licensePlateEntry = tk.Entry(inputFrame, text="Mašīnas numurzīme", font=("Calibri", 12))
    licensePlateEntry.grid(column=7, row=3)
    descriptionEntry= tk.Entry(inputFrame, text="Apraksts", font=("Calibri", 12))
    descriptionEntry.grid(column=8, row=3)

    #input button
    inputButton = tk.Button(inputFrame, text="Iesniegt klienta datus", command=dataInput , font=("Calibri", 12), relief="groove")
    inputButton. grid(column=4, columnspan=2, row=4, pady=20)

def dataInput():
    NewCar = Car(identificationNumber, formated_now, brandEntry.get(), modelEntry.get(), phoneNumberEntry.get(), winNumberEntry.get(), licensePlateEntry.get(), descriptionEntry.get())
    print(NewCar.__dict__)

root = tk.Tk()
root.geometry('1400x800')
root.resizable(False, False)
mainLog()
root.mainloop()
