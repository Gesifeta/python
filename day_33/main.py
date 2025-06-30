from tkinter import *
import os
import requests

file_diir = os.path.dirname(__file__)

window = Tk()
window.config(padx=50,pady=50)
window.title("Kanye says...")

canvas = Canvas(width=300,height=414)
background_image = PhotoImage(file=f"{file_diir}/background.png")
kanye_icon =  PhotoImage(file=f"{file_diir}/kanye.png")
canvas.create_image(150,207,image = background_image)
quote = canvas.create_text(150,207,text="dsdfweerwer",width=250, font=("Arial",15,"bold"), fill="white")

canvas.grid(column=1,row=0)

def get_quote():
    try:
        response = requests.get(url="https://api.kanye.rest")
    except ConnectionError:
        kanye_quote = "connection error"
        return kanye_quote
    else:
        kanye_quote = response.json()["quote"]
        canvas.itemconfig(quote, text = kanye_quote)
        return kanye_quote
    #Write your code here.
quote_button = Button(image=kanye_icon,command=get_quote)
quote_button.grid(column=1,row=1)


window.mainloop()