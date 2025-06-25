import tkinter as tk
from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
window = tk.Tk()
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(WORK_MIN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(WORK_MIN):
    canvas.itemconfig(timer_text, text=WORK_MIN)
    if WORK_MIN > 0:
        window.after(1000, count_down, WORK_MIN - 1)

# ---------------------------- UI SETUP ------------------------------- #

window.title("Pomodoro")
window.config(padx=20, pady=20,width=400,background=YELLOW, height=400)
title_label = Label(text="Timer",padx=10,pady=10, font=FONT_NAME , fg=GREEN, bg=YELLOW)
title_label.grid(column=4, row=0)
canvas  = Canvas(width=200, height = 224,bg =YELLOW,highlightthickness = 0)
import os
# Use absolute path to ensure the image is found
script_dir = os.path.dirname(os.path.abspath(__file__))
tomato_img_path = os.path.join(script_dir, "tomato.png")
tomato_image = PhotoImage(file=tomato_img_path)
canvas.create_image(100,112,   image = tomato_image)
timer_text= canvas.create_text(100, 130, text= WORK_MIN, fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=4, row=1)
start_button = Button(text="Start", font=FONT_NAME, command=start_timer)
start_button.grid(column=3, row=2)
reset_button = Button(text="Reset", font=FONT_NAME)
reset_button.grid(column=5, row=2)

window.mainloop()