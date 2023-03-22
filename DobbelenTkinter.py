#DobbelenTkinter Serkan

import tkinter as tk
import random

window = tk.Tk()
window.title("Dobbelen")

Label1 = tk.Label(
    height=5,
    width=50,
    text='Klik op "Random getal" om een random getal te maken!',
    font=("Arial", 30),
    background='#aa00ff'
)
Label1.pack(fill=tk.BOTH, expand=True)

Label2 = tk.Label(
    height=5,
    width=30,
    text='',
    font=("Arial", 40),
    background='#aa00ff'
)
Label2.pack(fill=tk.BOTH, expand=True)

submit = tk.Button(
    text="Random getal",
    background='white',
    font=("Arial", 18)   
)
submit.pack()

dobbelen = list(('1','2','3','4','5','6'))

def submitten(event):
    Label2['text'] = 'Het getal is: ' + random.choice(dobbelen) + '!'

submit.bind('<Button-1>', submitten)

clear = tk.Button(
    text="Clear",
    background='white',
    font=("Arial", 18)   
)
clear.pack(side='bottom')

def clearen(event):
    Label2['text'] = ''
    
clear.bind('<Button-1>', clearen)

frameBottom = tk.Frame(
    background='#aa00ff'
)
frameBottom.pack()
window.mainloop()