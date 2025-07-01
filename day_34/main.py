from question_model import Question
from data import get_quizes
from quiz_brain import Quiz
import html

questions = get_quizes()
quiz = Quiz(questions)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
