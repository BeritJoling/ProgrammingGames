import tkinter as tk
from tkinter import ttk

def easy():
    pass

def medium():
    pass

def hard():
    pass

def brutal():
    pass



window = tk.Tk()
window.title("Snake difficulty selection")

label = tk.Label(window, text="Select the difficulty:")
label.grid(row="0", columnspan=2, padx=5, pady=10)

easy_button = ttk.Button(window, text="Easy", command=easy())
easy_button.grid(row=1, column=1, padx=5, pady=5)

medium_button = ttk.Button(window, text="Medium", command=medium())
medium_button.grid(row=2, column=1, padx=5, pady=5)

hard_button = ttk.Button(window, text="Hard", command=hard())
hard_button.grid(row=3, column=1, padx=5, pady=5)

brutal_button = ttk.Button(window, text="Brutal", command=brutal())
brutal_button.grid(row=4, column=1, padx=5, pady=5)

