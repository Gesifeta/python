import html

from data import get_quizes
from quiz_brain import Quiz
import html
from ui import QuizUI

questions = get_quizes()
quiz = Quiz(questions)

def start_quiz():
    UI = QuizUI(quiz)
start_quiz()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
