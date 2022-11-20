from brain_games.engine import welcome_user, greet, rounds
import random
from random import randint

def generate_question():#generate of a question to the user
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    question = f'{number1} {operator} {number2}'
    if operator == '+':
        correct_answer = str(number1 + number2)
    elif operator == '-':
        correct_answer = str(number1 - number2)
    elif operator == '*':
        correct_answer = str(number1 * number2)
    return question, correct_answer



def calc():
    
    task = 'What is the result of the expression?'
    # question, correct_answer = generate_question()
    rounds(greet(welcome_user()), task, generate_question())
