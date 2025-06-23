# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
import os
import random
import pandas as pd
from tkinter import messagebox

window = Tk()
window.config(width =600,height = 600, padx=20,pady=20)
window.title("Password Manager")

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
username_entry.insert(0, "example@gmail.com")
password_label = Label(text="Password:")
password_entry = Entry(width=25)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate():
    password_entry.delete(0, END)
    password = []
    for _ in range(3):
      password.append(random.choice(symbols))
      password.append(random.choice(numbers))
    for _ in range(6):
      password.append(random.choice(letters))
      random.shuffle(password)
    password_entry.insert(0, ''.join(password))
# save entrie to a file
# first get text from entries
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        "website": [website],
        "username": [username],
        "password": [password]
    }
    # check if any of the entries are empty
    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?")
    # check if the file exists
    if not is_ok:
        return
    if os.path.exists("data.csv"):
        # if it exists, append the new data to the existing file
        df = pd.read_csv("data.csv")
        df = pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)
        df.to_csv("data.csv", index=False)
    else:
        # if it doesn't exist, create a new file and write the data to it
        df = pd.DataFrame(new_data)
        df.to_csv("data.csv", index=False)

    website_entry.delete(0, END)
    username_entry.delete(0,END)
    password_entry.delete(0, END)
    website_entry.focus()
add_button = Button(text="Add", width=36,command=save)
generate_button = Button(text="Generate",command=generate)

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