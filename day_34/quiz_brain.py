class Quiz:
    def __init__(self, questions) -> None:
        self.score = 0
        self.question_list = questions
        self.question_number = 0
        self.current_question = self.question_list[self.question_number]


    def right_answer(self):
        if self.current_question["correct_answer"] == "True":
            self.score +=1
            print(self.score)
            return True
    def wrong_answer(self):
        if self.current_question["correct_answer"] == "False":
            self.score +=1
            print(self.score)
            return True
        

    def still_has_questions(self):
        return self.question_number<len(self.question_list)


    def get_next_question(self):
         self.get_next_question = self.question_list[self.question_number]
         self.question_number += 1
         return self.current_question



    


