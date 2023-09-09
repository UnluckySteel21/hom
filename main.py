# Import tkinter and random modules
import tkinter as tk
import random

# Define the window size and title
window = tk.Tk()
window.title("Slot Machine Game")
window.geometry("300x200")

# Define the images for the slot machine symbols
images = ["🍒", "🍋", "🍇", "🍉", "🍊", "🍎"]

# Define the labels for the slot machine symbols
label1 = tk.Label(window, text="", font=("Arial", 50))
label2 = tk.Label(window, text="", font=("Arial", 50))
label3 = tk.Label(window, text="", font=("Arial", 50))

# Define the label for the result message
result = tk.Label(window, text="", font=("Arial", 20))

# Define the function to spin the slot machine
def spin():
    # Randomly select three symbols
    symbol1 = random.choice(images)
    symbol2 = random.choice(images)
    symbol3 = random.choice(images)

    # Display the symbols on the labels
    label1.config(text=symbol1)
    label2.config(text=symbol2)
    label3.config(text=symbol3)

    # Check if the symbols match and display the result message
    if symbol1 == symbol2 == symbol3:
        result.config(text="You win!", fg="green")
    else:
        result.config(text="You lose!", fg="red")

# Define the button to spin the slot machine
button = tk.Button(window, text="Spin", command=spin)

# Arrange the widgets on the window using grid layout
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)
result.grid(row=1, column=0, columnspan=3)
button.grid(row=2, column=0, columnspan=3)

# Start the main loop of the window
window.mainloop()
