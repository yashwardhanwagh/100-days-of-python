from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for ques in question_data:
    question_text = ques["text"]
    question_answer = ques["answer"]

    my_question = Question(question_text,question_answer)
    question_bank.append(my_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()
