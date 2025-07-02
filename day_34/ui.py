from tkinter import *
import os
import html


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
        self.question = self.canvas.create_text(150,150,width=250,text=html.unescape(self.quiz.current_question["question"]), fill="black",font=("Arial",15,"italic"))
        self.right = Button(image=self.right_image, command=self.is_true)
        self.wrong = Button(image=self.wrong_image, command=self.is_false)
        self.right.grid(column=0,row=3)
        self.wrong.grid(column=1,row=3)
        self.score_placeholder=Label(text=f"Score: {self.quiz.score}",pady=20,background=THEME_COLOR,fg="white")
        self.score_placeholder.grid(column=2,row=0)
        self.window.mainloop()

    def is_false(self):
            self.quiz.wrong_answer("False")
            self.canvas.itemconfig(self.question,text = self.quiz.current_question["question"])
            self.score_placeholder.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            if self.quiz.still_has_questions():
                   self.show_question(html.unescape(self.quiz.current_question["question"]))
            else:
                  self.canvas.itemconfig(self.question,text = "You reached the end of questions.")
           

    def is_true(self):
            self.quiz.right_answer("True")
            self.canvas.itemconfig(self.question,text = self.quiz.current_question["question"])
            self.score_placeholder.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            if self.quiz.still_has_questions():
                   self.show_question(html.unescape(self.quiz.current_question["question"]))
            else:
                  self.canvas.itemconfig(self.question,text = "You reached the end of questions.")
           

    def show_question(self, new_question):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question, text=new_question)
 