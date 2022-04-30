from email.mime import image
from tkinter import *
import math


# setup
root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)

# canvas
canvas = Canvas(width=200, height=200)
canvas.pack()
canvas.config()
logo = PhotoImage(file="padlock_logo_small.png")
canvas.create_image(100, 100, anchor=CENTER, image=logo)


# Labels



root.mainloop()
