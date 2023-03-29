#Tkinter Template 

#import tkinter ("as tk" zorgt ervoor dat ik niet over "tkinter" hoef in te vullen)
import tkinter as tk

#maakt een window instantie
window = tk.Tk()
window.title('getallen rader')

#maakt een label met een tekst
greeting = tk.Label(
    text="getal raden pssst het is 5.",
    #foreground is tekst kleur
    foreground="yellow",
    background="black",
    padx=50,
    pady=200,
    #eerst komt de font (zoals Arial, Calibri, Comic Sans MS etc) Daarna komt de grootte van de tekst (in dit geval 24)
    font=("Arial", 24)
)
#voegt een invoer veld toe
entry = tk.Entry(
    #De font is Arial en de tekstgrootte (en tekstbox) is 18
    font=("Arial", 18)
)

#plaats het label op het scherm met "pack" (Het word geplaatst op volgorde (dus eerst greeting en daarna entry))
greeting.pack()
entry.pack()

#start de event loop
window.mainloop()