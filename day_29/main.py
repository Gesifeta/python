# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window = Tk()
window.config(width =400,height = 600, padx=20,pady=20)
window.title("Password Manager")

import os
# Use absolute path to ensure the image is found
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_img_path = os.path.join(script_dir, "logo.png")
logo_image = PhotoImage(file=logo_img_path)
canvas  = Canvas(width=200,height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.pack()







window.mainloop()