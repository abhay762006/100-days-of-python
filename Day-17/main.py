from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank =[]
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    quiz = Question(question=question_text, answer=question_answer)
    question_bank.append(quiz)
quiz = QuizBrain(question_bank)
while quiz.still_question():
    next_question = quiz.next_question()

print("Quiz Completed")
print(f"Your final score was:{quiz.score}/{len(question_bank)} ")