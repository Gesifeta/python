from tkinter import *
import os

THEME_COLOR = "#375362"
file_path = os.path.dirname(__file__)
class QuizUI:
    def __init__(self) -> None:
        self.window = Tk()
        self.canvas = Canvas(width=400,height=600)
        self.right_image = PhotoImage(file=f"{file_path}/images/true.png")
        self.wrong_image = PhotoImage(file=f"{file_path}/images/false.png")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        self.canvas.create_image
        self.window.title("Trivia Quizes")
        
    


