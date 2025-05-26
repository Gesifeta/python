
class CheckAnswer:
    def __init__(self, user_response, answer):
        self.response = user_response
        self.correct_answer = answer
        if self.response == self.correct_answer:
            self.is_correct ="True"
        else:
            self.is_correct = "False"







