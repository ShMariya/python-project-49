
import random
from random import randint


OPERATORS = ['+', '-', '*']
TASK = 'What is the result of the expression?'


def get_answer(operator, number1, number2):
    if operator == '+':
        correct_answer = str(number1 + number2)
    elif operator == '-':
        correct_answer = str(number1 - number2)
    elif operator == '*':
        correct_answer = str(number1 * number2)
    return correct_answer


def get_question_correct_answer():  # generate of a question to the user
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    operator = random.choice(OPERATORS)
    question = f'Question: {number1} {operator} {number2}'
    return question, get_answer(operator, number1, number2)
