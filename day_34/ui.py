from tkinter import *
import os


THEME_COLOR = "#375362"
file_path = os.path.dirname(__file__)



class QuizUI():
    def __init__(self, quiz) -> None:
        self.quiz = quiz
        self.window = Tk()
        self.canvas = Canvas(width=300,height=325)
        self.right_image = PhotoImage(file=f"{file_path}/images/true.png")
        self.wrong_image = PhotoImage(file=f"{file_path}/images/false.png")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        self.window.title("Trivia Quizes")
        self.canvas.grid(column=0,row=1,columnspan=2,pady=(10,15))
        self.score_label = Label(text=f"Score: ",pady=20,background=THEME_COLOR,fg="white")
        self.score_label.grid(column=1,row=0)
        
        self.question = self.canvas.create_text(150,150,width=250,fill="black",font=("Arial",15,"italic"))
        self.right = Button(image=self.right_image,command=self.quiz.right_answer)
        self.wrong = Button(image=self.wrong_image,command=self.quiz.wrong_answer)
        self.right.grid(column=0,row=3)
        self.wrong.grid(column=1,row=3)
      
    def show_question(self, new_question):
        self.canvas.itemconfig(self.question, text=new_question)
        self.score_placeholder=Label(text=self.quiz.score,pady=20,background=THEME_COLOR,fg="white")
        self.score_placeholder.grid(column=2,row=0)
       
      

    
   
 


