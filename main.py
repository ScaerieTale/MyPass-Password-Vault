from tkinter import *
import math



# setup
root = Tk()
root.title("Password Manager")
root.config(bg="#00065f", padx=20, pady=20)

# # background
# space_bg = PhotoImage(file="space.png")
# background_label = Label(root, image=space_bg)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)


# canvas
canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1, columnspan=2)
canvas.config(bg="#00065f", highlightbackground="#FF9CFF")
logo = PhotoImage(file="MyPass_logo_small.png")
canvas.create_image(100, 100, anchor=CENTER, image=logo)


# Labels
web_label = Label(text="Website:")
web_label.config(anchor="e", fg="#ffa0ef", bg="#00065f", font=("times, serif", 18, ), )
web_label.grid(row=1, column=0)

email_label =  Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_label.config(anchor="e", fg="#ffa0ef", bg="#00065f", font=("times, serif", 18, ))

pass_label =  Label(text="Password:")
pass_label.grid(row=3, column=0)
pass_label.config(fg="#ffa0ef", bg="#00065f", font=("times, serif", 18, ))


root.mainloop()
