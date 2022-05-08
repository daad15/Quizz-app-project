from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
""""
*    Title: Quiz source code
*    Author: Udemy online Bootcamp, Dr.Angela Yu
*    Date: 2021
*    Availability: https://www.udemy.com/course/100-days-of-code/
"""
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
