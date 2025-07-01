class Quiz:
    def __init__(self, questions) -> None:
        self.score = 0
        self.question_list = questions
        self.question_number = 0
        self.current_question = self.question_list[self.question_number]["question"]


    def check_answer(self, answer):
        if self.current_question["correct_answer"] == answer:
            self.score +=1
            return True
        else:
            return False
        

    def still_has_questions(self):
        return self.question_number<len(self.question_list)


    def get_next_question(self):
         self.get_next_question = self.question_list[self.question_number]
         self.question_number += 1
         return self.current_question



    


