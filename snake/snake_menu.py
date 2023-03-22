import tkinter as tk
from tkinter import ttk
from snake import snake_easy

class snake_diff_window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Snake Difficulty Selection Menu")
        
        self.label = tk.Label(self, text="Select the difficulty to begin:")
        self.label.grid(row=0, columnspan=3, padx=5, pady=5)
        
        self.easy_start = ttk.Button(self, text="Easy", command=self.easy)
        self.easy_start.grid(row=1, column=1, padx=5, pady=5)
        
        self.medium_start = ttk.Button(self, text="Medium", command=self.medium)
        self.medium_start.grid(row=2, column=1, padx=5, pady=5)
        
        self.hard_start = ttk.Button(self, text="Hard", command=self.hard)
        self.hard_start.grid(row=3, column=1, padx=5, pady=5)
        
        self.brutal_start = ttk.Button(self, text="Brutal", command=self.brutal)
        self.brutal_start.grid(row=4, column=1, padx=5, pady=5)
    
    def easy(self):
        snake_easy.snake_easy()
        
        self.destroy()
    
    def medium(self):
        pass
    
    def hard(self):
        pass
    
    def brutal(self):
        pass
    