from data import question_data
class GenerateQuestion:
    def __init__(self, question_number):
        self.question = question_data[question_number]["text"]
        self.answer = question_data[question_number]["answer"]




