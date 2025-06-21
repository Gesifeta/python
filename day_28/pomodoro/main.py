import tkinter as tk
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=20, pady=20,width=400, height=400)
title_label = Label(text="Timer",padx=10,pady=10, font=FONT_NAME , fg=GREEN, bg=YELLOW)
title_label.grid(column=4,row=0)
canvas  = Canvas(width=200, height = 224,bg =YELLOW,highlightthickness = 0)
import os
# Use absolute path to ensure the image is found
script_dir = os.path.dirname(os.path.abspath(__file__))
tomato_img_path = os.path.join(script_dir, "tomato.png")
tomato_image = PhotoImage(file=tomato_img_path)
canvas.create_image(100,112,   image = tomato_image)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=4, row=1)

window.mainloop()