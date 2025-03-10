import tkinter as tk
from tkinter import messagebox
import math

# Function to handle button clicks
def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))  # Evaluate the expression
            entry.delete(0, tk.END)  # Clear the entry field
            entry.insert(tk.END, result)  # Display the result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif text == "C":
        entry.delete(0, tk.END)  # Clear the entry field
    elif text == "√":
        try:
            value = float(entry.get())
            if value >= 0:
                result = math.sqrt(value)
                entry.delete(0, tk.END)
                entry.insert(tk.END, result)
            else:
                messagebox.showerror("Error", "Cannot calculate square root of a negative number")
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif text == "x²":
        try:
            value = float(entry.get())
            result = value ** 2
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    else:
        entry.insert(tk.END, text)  # Add the button text to the entry field

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")  # Set the window size

# Create an entry field to display the input and result
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Define the buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
    "√", "x²"
]

# Create and place the buttons
frame = tk.Frame(root)
frame.pack()

row, col = 0, 0
for button in buttons:
    btn = tk.Button(frame, text=button, font=("Arial", 15), relief="raised", padx=20, pady=20)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", button_click)  # Bind the button click event
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main loop
root.mainloop()