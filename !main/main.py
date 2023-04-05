from tkinter import *
from DobbelenTkinter import *

# Maak een nieuw window met een titel
window = Tk()
window.title("Menu voorbeeld")

# Functies voor het menu
def show_thing_1():
    frame_thing_2.pack_forget()
    frame_thing_1.pack()

def show_thing_2():
    frame_thing_2.pack()
    frame_thing_1.pack_forget()

# Menu maken
menubar = Menu(window)
window.config(menu=menubar)

# Menu items maken
mainmenu = Menu(menubar)
mainmenu.add_command(label="Thing 1", command=show_thing_1)
mainmenu.add_command(label="Thing 2", command=show_thing_2)          
mainmenu.add_separator()
mainmenu.add_command(label="Exit", command=window.quit)
# Menu toevoegen aan menubar
menubar.add_cascade(label="Games",menu=mainmenu)

# FRAME VOOR THING 1 --------------------------------
frame_thing_1 = Frame(borderwidth=10)
label_1 = Label(frame_thing_1, text="THING 1", bg = "blue", fg="white", width=20, height=8)
label_1.pack()

# FRAME VOOR THING 2 --------------------------------
frame_thing_2 = Frame(borderwidth=10)
label_2 = Label(frame_thing_2, text="THING 2", bg="red", fg="yellow", width=20, height=8)
label_2.pack()

# MAIN --------------------------------
# Begin met frame 1
show_thing_1()
# Start the application
window.mainloop()