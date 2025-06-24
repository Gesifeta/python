
import os
import json
import pandas as pd
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
# set file directory
file_dir = os.path.dirname(__file__)
# window for the display
window = Tk()
window.config(width=600,height=1200,bg=BACKGROUND_COLOR,padx=50,pady=50)
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
canvas.create_image(405,270, image = card_front_image )
card_back_image = PhotoImage(file = f"{file_dir}/images/card_back.png")
canvas.grid(column=0,row=0,columnspan=2)

swedish_placeholder = Label(canvas,text="swedish",bg ="white", font=("Arial",40,"italic"))
swedish_placeholder.place(x=300,y=150)
english_placeholder = Label(canvas,text="english",bg ="white", font=("Arial",60,"bold"))
english_placeholder.place(x=300,y=263)

# buttons
right_image = PhotoImage(file=f"{file_dir}/images/right.png")
right_button = Button(window,image=right_image)
right_button.grid(column=1,row=2)

wrong_image = PhotoImage(file=f"{file_dir}/images/wrong.png")
wrong_button = Button(window,image=wrong_image)
wrong_button.grid(column=0,row=2)




window.mainloop()
