from collections import Counter

from data import question_data
from question_model import GenerateQuestion
from quiz_brain import CheckAnswer

def main():
    score = 0
    counter =0

    while counter < len(question_data):
        quizes = GenerateQuestion(counter)
        print(quizes.question)
        answer = input("Your Answer: ").lower()
        is_correct = CheckAnswer(answer, quizes.answer).is_correct.lower()
        if is_correct != 'false' and is_correct != 'true':
            print("Invalid input, quiz ended")
            break
        if is_correct == answer:
            score += 1
        counter += 1
    print(f"Your score is = {score}/{len(question_data)}")

main()

