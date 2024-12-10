import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def run_program():
    try:
        # Get the size of the array from the input field
        size = int(size_entry.get())
        if size <= 0:
            raise ValueError("Size must be a positive integer.")
        
        # Generate random integers between 0 and 5000
        random_numbers = np.random.randint(0, 5001, size)
        
        # Find the maximum and minimum values
        max_value = np.max(random_numbers)
        min_value = np.min(random_numbers)
        
        # Calculate the difference
        difference = max_value - min_value
        
        # Show results in a message box
        messagebox.showinfo(
            "Výsledky",
            f"Najvyššie číslo: {max_value}\n"
            f"Najnižšie číslo: {min_value}\n"
            f"Rozdiel: {difference}"
        )
        
        # Plot the difference as a bar chart
        plt.figure(figsize=(8, 4))
        plt.bar(['Difference'], [difference], color='skyblue')
        plt.title('Difference Between Max and Min Random Numbers')
        plt.ylabel('Value')
        plt.show()
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Programovacie techniky")

# Set window size and position
root.geometry("500x350")

# Create labels for program information
header_label = tk.Label(root, text="Programovacie techniky", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

author_label = tk.Label(root, text="Yaroslav Shulha", font=("Arial", 14))
author_label.pack(pady=5)

task_label = tk.Label(
    root,
    text=(
        "Zadanie úlohy:\n"
        "Vygenerujte pole náhodných celých čísiel od 0 do 5000,\n"
        "vypíšte najvyššie a najnižšie číslo a vypočítajte ich rozdiel,\n"
        "zobrazte graf hodnôt iba z rozdielov."
    ),
    font=("Arial", 12),
    justify="center",
)
task_label.pack(pady=10)

# Create an input field for the array size
size_label = tk.Label(root, text="Zadajte veľkosť poľa:", font=("Arial", 12))
size_label.pack(pady=5)
size_entry = tk.Entry(root, font=("Arial", 12), justify="center")
size_entry.pack(pady=5)
size_entry.insert(0, "34")  # Default size

# Create a button to run the program
run_button = tk.Button(root, text="Spustiť program", font=("Arial", 12), command=run_program)
run_button.pack(pady=20)

# Run the Tkinter main loop