from tkinter import*
from datetime import date


fenetre= Tk()

fenetre.title("age calculator")
fenetre.geometry("350x400")

def calculateAge():

    today = date.today()
    birth_date = date(int(year_entry.get()), int(month_entry.get()),int(day_entry.get()))
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    Label(text=f"Bonjour {name_value.get()}! VOTRE AGE EST: {age}", font=("arial", 15, "bold"), fg="green").grid(row=6, column=1)

Label(text="name", font=("arial", 15,"bold")).grid(row=1, column=0, padx=50)
Label(text="year", font=("arial", 15,"bold")).grid(row=2, column=0)
Label(text="month", font=("arial", 15,"bold")).grid(row=3, column=0)
Label(text="day", font=("arial", 15,"bold")).grid(row=4, column=0)

name_value= StringVar()
year_value= StringVar()
month_value= StringVar()
day_value= StringVar()

name_entry = Entry(fenetre, textvariable=name_value)
year_entry = Entry(fenetre, textvariable=year_value)
month_entry = Entry(fenetre, textvariable=month_value)
day_entry = Entry(fenetre, textvariable=day_value)

name_entry.grid(row=1, column=1, pady=5)
year_entry.grid(row=2, column=1, pady=5)
month_entry.grid(row=3, column=1, pady=5)
day_entry.grid(row=4, column=1, pady=5)

button = Button(text="Calculate age", font=("arial", 15, "bold"), fg="green", bg="#10100d", command=calculateAge)
button.grid(row=5,column=1, pady=5)

fenetre.mainloop()