# from brain_games.engine import welcome_user, greet, rounds
import random
from random import randint

task = 'Answer "yes" if the number is even, otherwise answer "no".'
game = 'even'

def generate_question_even():#generate of a question to the user
    
    number = randint(1, 100)
    question_even = f'Question: {number}'
    if number % 2 == 0:
        correct_answer_even = 'yes'
    else:
        correct_answer_even = 'no'
    return question_even, correct_answer_even



# def is_even():
    
#     # task = 'What is the result of the expression?'
#     # question, correct_answer = generate_question()
#     rounds(greet(welcome_user()), task, generate_question_even(), game)