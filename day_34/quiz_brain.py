class Quiz:
    def __init__(self, questions) -> None:
        self.score = 0
        self.question_list = questions
        self.question_number = 0
        self.current_question = self.question_list[self.question_number]


    def right_answer(self,answer):
        if self.current_question["correct_answer"] == answer and self.still_has_questions():
            self.score +=1
        if self.still_has_questions(): 
            self.question_number += 1
            self.get_next_question()
           
        return self.current_question["correct_answer"] == answer
            
    def wrong_answer(self, answer):
        if self.current_question["correct_answer"] == answer and self.still_has_questions(): 
            self.score +=1
        if self.still_has_questions():
            self.question_number += 1
            self.get_next_question()
            
        return self.current_question["correct_answer"] == answer

    def still_has_questions(self):
        return self.question_number < len(self.question_list)-1


    def get_next_question(self):
         self.current_question = self.question_list[self.question_number]
         return self.current_question



    


