from question_model import Question
from art import the_quiz
import os

class QuizBrain:


    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            user_answer = input(f"Q{self.question_number}. {current_question.text} (True/False)?: ").lower()
            if user_answer == "true" or user_answer == "false":
                self.check_answer(user_answer, current_question.answer)
                break
            else:
                os.system("cls")
                print(the_quiz)
                print('You must enter a valid option.\n')
                

                


    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was {correct_answer}")
        print(f"Score: {self.score}/{len(self.question_list)}")
        print("\n")