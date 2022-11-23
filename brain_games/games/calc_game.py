
import random
from random import randint


def generate_question_calc():  # generate of a question to the user
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    question = f'Question: {number1} {operator} {number2}'
    if operator == '+':
        correct_answer = str(number1 + number2)
    elif operator == '-':
        correct_answer = str(number1 - number2)
    elif operator == '*':
        correct_answer = str(number1 * number2)
    return question, correct_answer
