
import os
import json
import pandas as pd
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
FLASHES = 20
# set file directory
file_dir = os.path.dirname(__file__)
# window for the display
window = Tk()
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
window.title("Swedish Language Flash Card")
data = pd.read_csv(f"{file_dir}/data/Swedish.csv")

# with open(f"{file_dir}/data/swedish.txt", "r", encoding="utf-8") as new_file:
#     swedish_words = new_file.readlines()
#     swedish_words = [{"word":word.strip().split(" ")[0],"frequency":word.strip().split(" ")[1]} for word in swedish_words] 
# with open(f"{file_dir}/data/swedish.json", "w") as new_file:
#     json.dump(swedish_words, new_file, indent=4)

# Canvas setup
canvas= Canvas(width=800,height=526, highlightthickness =0)
canvas.config(bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file = f"{file_dir}/images/card_front.png")
card_back_image = PhotoImage(file = f"{file_dir}/images/card_back.png")
canvas.grid(column=0,row=0,columnspan=2)
background_image = canvas.create_image(405,270, image = card_front_image )
title = canvas.create_text(400,150, text="swedish", font=("Arial",30,"italic"))
meaning = canvas.create_text(400,263,text="english", font=("Arial",50,"bold"))


def start_flash():
    play_card(FLASHES)

def play_card(FLASH):
    random_word =random.randint(0, 35001)
    word = data.iloc[random_word]
    swedish = word["word"]
    english= word["english"]
    canvas.itemconfig(title,text="Swedish",)
    canvas.itemconfig(meaning,text=swedish)
    canvas.itemconfig(background_image,image = card_front_image)
    def show_answer():
        canvas.itemconfig(background_image,image = card_back_image)
        canvas.itemconfig(title,text="English",)
        canvas.itemconfig(meaning,text=english)
    window.after(3000,show_answer)

    if FLASH>0:
         FLASH  -= 1
         window.after(6000, play_card,FLASH)


# buttons
right_image = PhotoImage(file=f"{file_dir}/images/right.png")
right_button = Button(window, image=right_image)
right_button.grid(column=1,row=2)

wrong_image = PhotoImage(height=100,width=100,file=f"{file_dir}/images/wrong.png")
wrong_button = Button(window,image=wrong_image)
wrong_button.grid(column=0,row=2)


start_flash()

window.mainloop()
