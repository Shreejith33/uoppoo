from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("400x400")
number = Label(root)

number = random.sample(range (50, 100), 1)
number.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()