class Quiz:
    def __init__(self, questions) -> None:
        self.score = 0
        self.question_list = questions
        self.question_number = 0
        self.current_question = self.question_list[self.question_number]
    

    
