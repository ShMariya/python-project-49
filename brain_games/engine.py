import prompt
import random
from random import randint

def welcome_user():
    name = prompt.string('May I have your name? ')
    return name


# task = 'What is the result of the expression?'
# question = '5 + 6'
# correct_answer = str(11)


def greet(name):
    print(f'Hello, {name}!')
    return name


# greet(welcome_user())
# print(greet(welcome_user()))



# def generate_question():#generate of a question to the user
#     number1 = randint(1, 50)
#     number2 = randint(1, 50)
#     operators = ['+', '-', '*']
#     operator = random.choice(operators)
#     question = f'{number1} {operator} {number2}'
#     if operator == '+':
#         correct_answer = str(number1 + number2)
#     elif operator == '-':
#         correct_answer = str(number1 - number2)
#     elif operator == '*':
#         correct_answer = str(number1 * number2)
#     return question, correct_answer
def generate_question():
    pass

def rounds(name, task, question_correct_answer):
    print(task)
    for i in range(3):
        question, correct_answer = question_correct_answer
        print(question)
        answer = input()
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'. \
Let's try again, {name}!")
            break

        else:
            print('Correct!')
            i += 1
        if i == 3:
            print(f'Congratulations, {name}!')
    
# rounds(greet(welcome_user()), task, generate_question())