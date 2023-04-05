#De main pagina voor enidopdracht grogrammeren p3

#importeert tkinter. "tk" zorgt ervoor dat je "tkinter" niet de hele tijd hoeft in te vullen
import tkinter as tk

#maakt een window aan met de naam "Main Pagina"
window = tk.Tk()
window.title("Main Pagina")

#voegt text toe dat ook de achtergrond is voor de window
Label1 = tk.Label(
    height=5,
    width=30,
    text='Main pagina programmeren \n ↓↓↓ Ontspannings tools  ↓↓↓',
    font=("Arial", 30),
    background='#ff7729',
    foreground='white'
)
#dit zorgt ervoor dat de achtergrond volledig word gevuld
Label1.pack(fill=tk.BOTH, expand=True)

#Boter Kaas en Eieren
bte = tk.Button(
    text="Boter Kaas en Eieren",
    background='white',
    font=("Arial", 18)   
)
bte.pack(side='left')

#Coin Flip
cf = tk.Button(
    text="Coinflip",
    background='white',
    font=("Arial", 18)   
)
cf.pack(side='left')

#Dobbelen
db = tk.Button(
    text="Dobbelen",
    background='white',
    font=("Arial", 18)   
)
db.pack(side='left')

#Getallen Rader
gr = tk.Button(
    text="Getallen Rader",
    background='white',
    font=("Arial", 18)   
)
gr.pack(side='left')

#Snake
sn = tk.Button(
    text="Snake",
    background='white',
    font=("Arial", 18)   
)
sn.pack(side='left')


#Buttons Binden

def boterkaaseieren(event):
    print('Boter Kaas en Eieren')
    #Hier moet ik nog ff kijken hoe ik die shit kan linken

bte.bind('<Button-1>', boterkaaseieren)


def coinflip(event):
    print('Coin Flip')
    #Hier moet ik nog ff kijken hoe ik die shit kan linken

cf.bind('<Button-1>', coinflip)

def dobbelen(event):
    print('Dobbelen')
    #Hier moet ik nog ff kijken hoe ik die shit kan linken

db.bind('<Button-1>', dobbelen)

def getallenrader(event):
    print('Getallen Rader')
    #Hier moet ik nog ff kijken hoe ik die shit kan linken

gr.bind('<Button-1>', getallenrader)

def snake(event):
    print('Snake')
    #Hier moet ik nog ff kijken hoe ik die shit kan linken

sn.bind('<Button-1>', snake)


window.mainloop()