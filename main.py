from tkinter import *
from tkinter import messagebox
from random import randint
import random
import pyperclip

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


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields blank :-)")    
    else:
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


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    
    letters_list =[random.choice(letters) for _ in range(nr_letters)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = letters_list + numbers_list + symbols_list
    random.shuffle(password_list)    
    generated_password = "".join(password_list)
    
    pass_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# Buttons
gen_button_img = PhotoImage(file="generate_password_button.png")
gen_pass_button = Button(image=gen_button_img, height=60, width=205, bg=BG_COLOR, command=generate)
gen_pass_button.grid(row=3, column=2, columnspan=2)

entry_button_img = PhotoImage(file="add_entry.png")
add_entry_button = Button(image= entry_button_img, height=60, bg=BG_COLOR, command=save)
add_entry_button.grid(row=4, column=1)



root.mainloop()
