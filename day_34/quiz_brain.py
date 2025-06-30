class Quiz:
    def __init__(self, questions) -> None:
        self.score = 0
        self.question_list = questions
        self.question_number = 0
        self.current_question = self.question_list[self.question_number]


    def check_answer(self, answer):
        if self.current_question["answer"] == answer:
            self.score +=1
            return True
        else:
            return False
        
        
    def get_next_question(self):
         self.question_number += 1



    


