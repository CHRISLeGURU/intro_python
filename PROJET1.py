
from tkinter import *
#creation d'une fonction

def action():
    N=int(entryNombre1.get())
    N2 =2*N
    entryNombre2.delete(0, END)
    entryNombre2.insert(0, N2)

fen=Tk()
fen.geometry("400x300")
lblNombre1 = Label(fen, text ="Saisissez la valeur de N")
lblNombre1.place(x = 50,  y = 50 )
entryNombre1 = Entry(fen)
entryNombre1.place(x = 200 , y = 50)

lblNombre2 = Label(fen, text ="Voici le double")
lblNombre2.place(x = 50,  y = 100 )
entryNombre2 = Entry(fen)
entryNombre2.place(x = 200 , y = 100)
 
Valider = Button(fen, text="Valider l'operation", command = action)
Valider.place(x =200, y = 150)
fen.mainloop()
