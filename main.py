from lib2to3.pgen2.token import BACKQUOTE
from tkinter import *
import math

BG_COLOR = "#00056f"
FG_COLOR = "#ffa0ff"


# setup
root = Tk()
root.title("Password Manager")
root.config(bg=BG_COLOR, padx=20, pady=20)

# # background
# space_bg = PhotoImage(file="space.png")
# background_label = Label(root, image=space_bg)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)


# canvas
canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1, columnspan=2)
canvas.config(bg="#00065f", highlightbackground=FG_COLOR)
logo = PhotoImage(file="MyPass_logo_small.png")
canvas.create_image(100, 100, anchor=CENTER, image=logo)


# Labels
web_label = Label(text="Website:")
web_label.config(anchor="e", fg=FG_COLOR, bg=BG_COLOR, font=("times, serif", 18, ), )
web_label.grid(row=1, column=0)

email_label =  Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_label.config(bg=BG_COLOR, fg=FG_COLOR, font=("times, serif", 18, ))

pass_label =  Label(text="Password:")
pass_label.grid(row=3, column=0)
pass_label.config(fg=FG_COLOR, bg=BG_COLOR, font=("times, serif", 18, ))


# Entries
web_entry = Entry(width=35, bg=BG_COLOR, fg=FG_COLOR, font=("times, serif", 18, ))
web_entry.grid(row=1, column=1)
email_entry =  Entry(width=35, fg=BG_COLOR, font=("times, serif", 18, ))
email_entry.grid(row=2, column=1)
pass_entry = Entry(width=21, bg=BG_COLOR, fg=FG_COLOR, font=("times, serif", 18, ))
pass_entry.grid(row=3, column=1)


# Buttons
gen_button_img = PhotoImage(file="generate_password_button.png")
gen_pass_button = Button(image=gen_button_img)
gen_pass_button.grid(row=3, column=2, columnspan=2)




root.mainloop()
