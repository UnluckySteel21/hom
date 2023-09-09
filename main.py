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

# Define the label for the point system
points = tk.Label(window, text="", font=("Arial", 20))

# Define the variable to store the current points
current_points = tk.IntVar()

# Define the function to ask for the preferred points at the start of the game
def ask_points():
    # Create a new window to ask for the preferred points
    ask_window = tk.Toplevel(window)
    ask_window.title("Enter your preferred points")
    ask_window.geometry("200x100")

    # Create a label to instruct the user
    instruction = tk.Label(ask_window, text="Enter a positive integer:")
    
    # Create an entry to get the user input
    entry = tk.Entry(ask_window)

    # Create a function to validate the user input and set the current points
    def validate():
        # Get the user input as a string
        input = entry.get()

        # Check if the input is a positive integer
        if input.isdigit() and int(input) > 0:
            # Set the current points to the input value
            current_points.set(int(input))

            # Display the current points on the label
            points.config(text=f"Points: {current_points.get()}")

            # Destroy the ask window
            ask_window.destroy()
        else:
            # Display an error message on the label
            instruction.config(text="Invalid input. Try again.")

    # Create a button to submit the user input
    submit = tk.Button(ask_window, text="Submit", command=validate)

    # Arrange the widgets on the ask window using grid layout
    instruction.grid(row=0, column=0, columnspan=2)
    entry.grid(row=1, column=0)
    submit.grid(row=1, column=1)

# Define the function to spin the slot machine
def spin():
    # Check if there are enough points to play
    if current_points.get() > 0:
        # Deduct one point from the current points
        current_points.set(current_points.get() - 1)

        # Display the updated points on the label
        points.config(text=f"Points: {current_points.get()}")

        # Randomly select three symbols
        symbol1 = random.choice(images)
        symbol2 = random.choice(images)
        symbol3 = random.choice(images)

        # Display the symbols on the labels
        label1.config(text=symbol1)
        label2.config(text=symbol2)
        label3.config(text=symbol3)

        # Check if the symbols match and display the result message and update the points accordingly
        if symbol1 == symbol2 == symbol3:
            result.config(text="You win!", fg="green")

            # Add ten points to the current points
            current_points.set(current_points.get() + 10)

            # Display the updated points on the label
            points.config(text=f"Points: {current_points.get()}")
        else:
            result.config(text="You lose!", fg="red")
    else:
        # Display a message that there are no more points left
        result.config(text="No more points!", fg="black")

# Define the button to spin the slot machine
button = tk.Button(window, text="Spin", command=spin)

# Arrange the widgets on the window using grid layout
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)
result.grid(row=1, column=0, columnspan=3)
points.grid(row=2, column=0, columnspan=3)
button.grid(row=3, column=0, columnspan=3)

# Ask for the preferred points at the start of the game
ask_points()

# Start the main loop of the window
window.mainloop()