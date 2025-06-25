
import os
import json
import pandas as pd
from tkinter import *
import random
import datetime

BACKGROUND_COLOR = "#B1DDC6"
FLASHES = 5

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
current = datetime.datetime.now()

scores ={
    current.strftime("%A"):{
        "wrong":0,
        "right":0
    }
}


def wrong_score():
    scores[current.strftime("%A")]["wrong"] += 1
    try:
        new_score= open(f"{file_dir}/data/score.json","r")
    except FileNotFoundError:
        with  open(f"{file_dir}/data/score.json","w") as new_score:
            json.dump(scores,new_score)
    else:
        json_data = json.load(new_score)
        print(json_data)
        json_data.update(scores)
        with open(f"{file_dir}/data/score.json","w") as new_score:
            json.dump(json_data,new_score,indent=4)

def right_score():
    scores[current.strftime("%A")]["right"] += 1
    try:
        new_score= open(f"{file_dir}/data/score.json","r")
    except FileNotFoundError:
        with  open(f"{file_dir}/data/score.json","w") as new_score:
            json.dump(scores,new_score)
    else:
        json_data = json.load(new_score)
        json_data.update(scores)
        with open(f"{file_dir}/data/score.json","w") as new_score:
            json.dump(json_data,new_score,indent=4)
  
def save_score():
    try:
            data_json = open(f"{file_dir}/data/score.json","r")
    except FileNotFoundError:
        with open(f"{file_dir}/data/score.json","w") as new_score:
            json.dump(scores, new_score,indent=4)
    else:
         score = json.load(data_json)
         score.update(scores)
         with open(f"{file_dir}/data/score.json","w") as new_score:
             json.dump(score, new_score,indent=4)
def start_flash():
    play_card(FLASHES)
    save_score()

def play_card(FLASH):
    random_word =random.randint(0, 35001)
    word = data.iloc[random_word]
    swedish = word["word"]
    english= word["english"]
    canvas.itemconfig(title,text="Swedish",fill = "black")
    canvas.itemconfig(meaning,text=swedish,fill = "black")
    canvas.itemconfig(background_image,image = card_front_image)
    def show_answer():
        canvas.itemconfig(background_image,image = card_back_image)
        canvas.itemconfig(title,text="English", fill="white")
        canvas.itemconfig(meaning,text=english, fill ="white")
    window.after(3000,show_answer)

    if FLASH>0:
         FLASH  -= 1
         window.after(6000, play_card,FLASH)

# buttons
right_image = PhotoImage(file=f"{file_dir}/images/right.png")
right_button = Button(window, image=right_image,command=right_score)
right_button.grid(column=1,row=2)

wrong_image = PhotoImage(height=100,width=100,file=f"{file_dir}/images/wrong.png")
wrong_button = Button(window,image=wrong_image, command=wrong_score)
wrong_button.grid(column=0,row=2)


start_flash()

window.mainloop()
