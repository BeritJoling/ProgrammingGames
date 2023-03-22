import tkinter as tk
from tkinter import ttk
import random

class snake_easy(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Snake | Easy | Score: ")
        
        self.placeholder = tk.Label(self, text="PLACEHOLDER")
        self.placeholder.grid(row=1, column=1, padx=10, pady=10)