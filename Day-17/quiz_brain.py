class QuizBrain:
    def __init__(self, q_list):
        self.questions_number = 0
        self.question_list = q_list
        self.score = 0
    def still_question(self):
        if self.questions_number < len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        current_question = self.question_list[self.questions_number]
        self.questions_number += 1
        user_answer = input(f"Q.{self.questions_number}: {current_question.question} (True/False)")
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Your score is {self.score}/{self.questions_number}")

        else:
            print("You got it wrong!")

            print(f"Your score is {self.score}/{self.questions_number}")
        print(f"Correct answer: {correct_answer}")
        print("\n")