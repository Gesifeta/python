from tkinter import *
import os

THEME_COLOR = "#375362"
file_path = os.path.dirname(__file__)
class QuizUI:
    def __init__(self) -> None:
        self.window = Tk()
        self.canvas = Canvas(width=300,height=325)
        self.right_image = PhotoImage(file=f"{file_path}/images/true.png")
        self.wrong_image = PhotoImage(file=f"{file_path}/images/false.png")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        self.window.title("Trivia Quizes")
        self.canvas.grid(column=0,row=1,columnspan=2)
        self.score_label = Label(text=f"Score: /10",pady=20,background=THEME_COLOR,fg="white")
        self.score_label.grid(column=1,row=0)
        self.right = Button(image=self.right_image,pady=10,background=THEME_COLOR,highlightthickness=0)
        self.right.grid(row=2,column=0)
        self.wrong = Button(image=self.wrong_image,pady=10,background=THEME_COLOR,highlightthickness=0)
        self.wrong.grid(row=2,column=1)
    def show_question(self, question):
        self.canvas.create_text(150,150, text=question,width=250,fill="black",font=("Arial",15,"italic"))

        
        self.window.mainloop()


