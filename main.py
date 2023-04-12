import tkinter as tk
from tkinter import ttk
from snake import snake_menu
from getallenraden import rohaneindopdracht

class window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Main Menu")
        
        self.main_label = tk.Label(self, text="This is the main menu, select the game you'd like to play from the buttons below.")
        self.main_label.grid(row=1, columnspan=3, padx=5, pady=10)
        
        self.game1_start = ttk.Button(self, text="game1", command=self.game1)
        self.game1_start.grid(row=2, column=1, padx=5, pady=5)
        
        self.game2_start = ttk.Button(self, text="Snake", command=self.game2)
        self.game2_start.grid(row=3, column=1, padx=5, pady=5)
        
        self.game3_start = ttk.Button(self, text="Number Guessing", command=self.game3)
        self.game3_start.grid(row=4, column=1, padx=5, pady=5)
        
        self.game4_start = ttk.Button(self, text="Game4", command=self.game4)
        self.game4_start.grid(row=5, column=1, padx=5, pady=5)
        
        self.game5_start = ttk.Button(self, text="Game5", command=self.game5)
        self.game5_start.grid(row=6, column=1, padx=5, pady=5)
        
    def game1(self):
        pass
    
    def game2(self):
        snake_menu.snake_diff_window()
        
        self.destroy()
        
    def game3(self):
        rohaneindopdracht.GuessingGame()
        
        self.destroy
    
    def game4(self):
        pass
    
    def game5(self):
        pass
    

root = window()
root.mainloop()
