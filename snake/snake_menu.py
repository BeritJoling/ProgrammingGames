import tkinter as tk
from tkinter import ttk
import subprocess
import os


cwd = os.path.dirname(os.path.abspath(__file__))

class snake_diff_window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Snake Difficulty Selection Menu")
        
        self.label = tk.Label(self, text="Select the difficulty to begin:")
        self.label.grid(row=0, columnspan=3, padx=5, pady=5)
        
        self.easy_start = ttk.Button(self, text="Easy", command=self.easy)
        self.easy_start.grid(row=1, column=1, padx=5, pady=5)
        
        self.medium_start = ttk.Button(self, text="Normal", command=self.normal)
        self.medium_start.grid(row=2, column=1, padx=5, pady=5)
        
        self.hard_start = ttk.Button(self, text="Hard", command=self.hard)
        self.hard_start.grid(row=3, column=1, padx=5, pady=5)
        
        self.brutal_start = ttk.Button(self, text="Brutal", command=self.brutal)
        self.brutal_start.grid(row=4, column=1, padx=5, pady=5)
    
    def easy(self):
        subprocess.Popen(["python", "%s\\snake_easy.py"%cwd])
        
        self.destroy()
    
    def normal(self):
        subprocess.Popen(["python", "%s\\snake_normal.py"%cwd])
        
        self.destroy()
    
    def hard(self):
        subprocess.Popen(["python", "%s\\snake_hard.py"%cwd])
        
        self.destroy()
    
    def brutal(self):
        subprocess.Popen(["python", "%s\\snake_brutal.py"%cwd])
        
        self.destroy