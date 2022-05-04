from tkinter import *
from tkinter import messagebox

BG_COLOR = "#00054f"
FG_COLOR = "#cfe0b0"


# setup
root = Tk()
root.title("MyPass Password Manager")
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
web_label = Label(text="Website:", height=2)
web_label.config(anchor="e", fg=FG_COLOR, bg=BG_COLOR, font=("times, serif", 18, ), )
web_label.grid(row=1, column=0)

email_label =  Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_label.config(bg=BG_COLOR, fg=FG_COLOR, font=("times, serif", 18, ))

pass_label =  Label(text="Password:")
pass_label.grid(row=3, column=0)
pass_label.config(fg=FG_COLOR, bg=BG_COLOR, font=("times, serif", 18, ))


# Entries
web_entry = Entry(width=48, fg=BG_COLOR, font=("times, serif", 18, ))
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
email_entry =  Entry(width=48, fg=BG_COLOR, font=("times, serif", 18, ))
email_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=30, fg=BG_COLOR, font=("times, serif", 18, ))
pass_entry.grid(row=3, column=1)


#functions
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    is_ok = messagebox.askokcancel(title=website, message=f"Is this correct?\n{email}\n{password}")

    if is_ok:
        with open("data.txt", 'a') as password_file:
            password_file.write(f"""
        
Website: {website}
Username: {email}
Password: {password}""")
        web_entry.delete(0, END)
        email_entry.delete(0, END)
        pass_entry.delete(0, END)



# Buttons
gen_button_img = PhotoImage(file="generate_password_button.png")
gen_pass_button = Button(image=gen_button_img, height=60, width=205, bg=BG_COLOR)
gen_pass_button.grid(row=3, column=2, columnspan=2)

entry_button_img = PhotoImage(file="add_entry.png")
add_entry_button = Button(image= entry_button_img, height=60, bg=BG_COLOR, command=save)
add_entry_button.grid(row=4, column=1)



root.mainloop()
