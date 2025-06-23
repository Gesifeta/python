# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window = Tk()
window.config(width =600,height = 600, padx=20,pady=20)
window.title("Password Manager")

import os
# Use absolute path to ensure the image is found
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_img_path = os.path.join(script_dir, "logo.png")
logo_image = PhotoImage(file=logo_img_path)
canvas  = Canvas(width=200,height=200)
canvas.create_image(100, 100, image=logo_image)

website_label = Label(text="Website:")
website_entry = Entry(width=35)
website_entry.focus()
username_label = Label(text="Email/Username:")
username_entry = Entry(width=35)
password_label = Label(text="Password:")
password_entry = Entry(width=25)
generate_button = Button(text="Generate")
add_button = Button(text="Add")

# place items on the grid
canvas.grid(column=1, row=0)
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, columnspan=2)
username_label.grid(column=0, row=2)
username_entry.grid(column=1, row=2, columnspan=2)
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)    
generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)








window.mainloop()