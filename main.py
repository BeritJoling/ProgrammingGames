import tkinter as tk
from tkinter import ttk

#Functions to be executed when the respective button is pressed for switching frames
def game1():
    pass

def game2():
    pass

def game3():
    pass

def game4():
    pass

def game5():
    pass



#Start the first window
window = tk.Tk()
window.title("Main Menu")

#General explanation label
main_label = tk.Label(window, text="This is the main menu, select the game you'd like to play from the buttons below.")
main_label.grid(row=0, columnspan=3, padx=5, pady=10)

#Label and button for the first game
game1_label = tk.Label(window, text="Game1")
game1_label.grid(row=1, column=1, padx=5)
game1_button = tk.Button(window, text="Start", command=game1())
game1_button.grid(row=2, column=1, padx=5, pady=10)

#Label and button for the second game
game2_label = tk.Label(window, text="Game2")
game2_label.grid(row=1, column=2, padx=5)
game2_button = tk.Button(window, text="Start", command=game2())
game2_button.grid(row=2, column=2, padx=5, pady=10)

#Label and button for the third game
game3_label = tk.Label(window, text="Game3")
game3_label.grid(row=1, column=3, padx=5)
game3_button = tk.Button(window, text="Start", command=game3())
game3_button.grid(row=2, column=3, padx=5, pady=10)

#Label and button for the forth game
game4_label = tk.Label(window, text="Game4")
game4_label.grid(row=1, column=4, padx=5)
game4_button = tk.Button(window, text="Start", command=game4())
game4_button.grid(row=2, column=4, padx=5, pady=10)

#label and button for the fifth game
game5_label = tk.Label(window, text="Game5")
game5_label.grid(row=1, column=5, padx=5)
game5_button = tk.Button(window, text="Start", command=game5())
game5_button.grid(row=2, column=5, padx=5, pady=10)


#Initialize the program
window.mainloop()