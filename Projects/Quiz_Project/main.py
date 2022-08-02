from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from art import the_quiz, quiz_finished

question_bank = []

for entry in question_data:
    new_question = Question(entry["text"], entry["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
print(the_quiz)
print("Welcome to The Quiz!")
while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz! ")
print(quiz_finished)